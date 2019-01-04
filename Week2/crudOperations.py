import pymongo


client = pymongo.MongoClient("mongodb+srv://kenalger:SuperPassword@blog-i6lut.mongodb.net/test?retryWrites=true")

blogDatabase = client.blog
usersCollection = blogDatabase.users
articlesCollection = blogDatabase.articles

randomUser = usersCollection.find_one()

print(randomUser)

karmaCount = usersCollection.find({"karma": {"$gte": 450, "$lte": 475}}).count()

print(karmaCount)

# Add Comments to an article

articlesCollection.update({"_id": 19}, {"$set": {"comments": []}})

# Update Comments

articlesCollection.update({"_id": 19},
                          {"$push": {"comments":
                                         {"username": "mary",
                                          "comment": "Great first post."}}})

# Delete Article

articlesCollection.remove({"_id": 25})


