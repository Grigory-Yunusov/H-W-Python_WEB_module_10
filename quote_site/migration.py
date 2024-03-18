# import os
# import django
# import configparser

# from pymongo import MongoClient
# # from connect import connect_to_db

# # connect_to_db()

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quote_site.settings')
# django.setup()

# from quotes.models import Quote, Tag, Author

# config = configparser.ConfigParser()
# config.read('config.ini')
# mongo_user = config.get('DB', 'user')
# mongodb_pass = config.get('DB', 'pass')
# db_name = config.get('DB', 'db_name')
# domain = config.get('DB', 'domain')
# client = MongoClient(f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority", ssl=True)

# db = client.hw

# authors = db.author.find()

# for author in authors:
#     print(author)