import pymongo


# replace <PASSWORD> with user password
client = pymongo.MongoClient("mongodb+srv://kenalger:SuperPassword@blog-i6lut.mongodb.net/test?retryWrites=true")

blogDatabase = client.blog
usersCollection = blogDatabase.users

ken = {
    "username": "kalger",
    "password": "password",
    "lang": "EN"
}

usersCollection.insert_one(ken)

user = usersCollection.find_one()

print(user)

