import pymongo
import pprint

from pymongo.errors import ConnectionFailure

# replace <PASSWORD> with user password
client = pymongo.MongoClient("mongodb+srv://kenalger:SuperPassword@blog-i6lut.mongodb.net/test?retryWrites=true")

try:
    status = client.admin.command("serverStatus")
    print("Connected to MongoDB Atlas with status: ")
    pprint.pprint(status)

except ConnectionFailure:
    print("MongoDB Atlas connection not established.")
