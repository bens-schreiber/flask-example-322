from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://root:example@localhost:27017/')

# Grab the bob-ross-db database
db = client['baz-db']

def get_baz_from_db():
    # Get baz from the db
    baz = db.baz.find_one()["baz"]
    return baz

def update_baz_in_db(baz):
    # update baz in the db
    db.baz.update_one({}, {"$set": {"baz": baz}})
    return baz
