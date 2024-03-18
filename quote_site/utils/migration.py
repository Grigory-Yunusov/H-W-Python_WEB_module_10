import os 
import django
import configparser
from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quote_site.settings")
django.setup()

from quotes.models import Quote, Tag, Author # noqa

config = configparser.ConfigParser()
config.read('config.ini')
mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')
client = MongoClient(f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority", ssl=True)

db = client.hw

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )
quotes = db.quote.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    

    exist_quote = bool(len(Quote.objects.filter(quote = quote['quote'])))

    if not exist_quote:
        author = db.author.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        ) 
        for tag in tags:
            q.tags.add(tag)