import pymongo

client = pymongo.MongoClient("mongodb+srv://nhha:wVguGvkacYv5xp2D@cluster0-iwkgo.mongodb.net/test?retryWrites=true")
db = client.bike

def add_bike(a,b,c,d):
    db.bike.insert_one({
        'model' : a,
        'fee' : b,
        'image_url' : c,
        'year' : d
    })

def all_bike():
    return list(db.bike.find())