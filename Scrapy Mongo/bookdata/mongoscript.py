from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://test:AkibNayan2@cluster0.dt5i7bu.mongodb.net/")
db = client.scrapy
posts = db.test_collection

doc = post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}
post_id = posts.insert_one(post).inserted_id
print(post_id)
