import datetime
import pymongo
import random
import string


def randomString(size, letters=string.ascii_letters):
    return "".join([random.choice(letters) for _ in range(size)])


def makeArticle(count):
    return {
        "_id": count,
        "title": "Title " + str(count),
        "body": randomString(80),
        "author": "USER_" + str(random.randrange(0,999999)),
        "posted": datetime.datetime.now()
    }


def makeUser(count):
    return {
        "_id": "USER_" + str(count),
        "password": randomString(10),
        "karma": random.randint(0, 500),
        "registered": datetime.datetime.now(),
        "lang": "EN"
    }


client = pymongo.MongoClient("mongodb+srv://kenalger:SuperPassword@blog-i6lut.mongodb.net/test?retryWrites=true")

blogDatabase = client.blog
usersCollection = blogDatabase.users
articlesCollection = blogDatabase.articles

usersCollection.drop()
articlesCollection.drop()

users = []
count = 0
for i in range(100000):
    users.append(makeUser(i))
    if (len(users) % 1000) == 0:
        usersCollection.insert_many(users)
        count = count + 1000
        print("Inserted {} users".format(count))
        users = []

articles = []
count = 0

for i in range(100000):
    articles.append(makeArticle(i))
    if (len(articles) % 1000) == 0:
        articlesCollection.insert_many(articles)
        count = count + 1000
        print("Inserted {} articles".format(articles))
        articles = []
