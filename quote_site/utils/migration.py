import os 
import django
import json
import configparser
from pymongo import MongoClient
from mongoengine import connect
from datetime import datetime


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quote_site.settings")
django.setup()

from quotes.models import Quote, Tag, Author # noqa

config = configparser.ConfigParser()
config.read('utils/config.ini')
mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')
client = MongoClient(f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority", ssl=True)

db = client.GrigoryCluster

authors = db.author.find()

for author in authors:

    print(author)
    corecte_date = datetime.strptime(author.get('born_date'), '%B %d, %Y')
    born_date = corecte_date.strftime('%Y-%m-%d') 
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=born_date,
        born_location=author['born_location'],
        description=author['description']
    )
quotes = db.quote.find()

for quote in quotes:
    print(quote)
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
        
    

    exist_quote = bool(len(Quote.objects.filter(quote = quote['quote'])))

    if not exist_quote:
        author = db.author.find_one({'_id': quote['author']})
        if not author:
            continue
        a = Author.objects.filter(fullname=author['fullname']).first()
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        ) 
        for tag in tags:
            q.tags.add(tag)
            

author_data = []
for author in authors:
    print(author)
    author_data.append({
        'fullname': author['fullname'],
        'born_date': author['born_date'],
        'born_location': author['born_location'],
        'description': author['description']
    })

with open('author.json', 'w') as f:
    json.dump(author_data, f)


quote_data = []
for quote in quotes:
    author = db.author.find_one({'_id': quote['author']})
    quote_data.append({
        'quote': quote['quote'],
        'author': author['fullname'],
        'tags': quote['tags']
    })

with open('quotes.json', 'w') as f:
    json.dump(quote_data, f)