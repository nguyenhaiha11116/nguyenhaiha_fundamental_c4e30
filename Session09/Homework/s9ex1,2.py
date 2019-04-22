import pymongo

client = pymongo.MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db=client.c4e

db.posts.insert_one({
    'title' : 'c4e khóa 30',
    'author' : 'Nguyễn Hải Hà',
    'content' : 'Giáo viên tâm huyết,trợ giảng tốt bụng,học viên thì max đẹp trai!!!'
})

print(list(db.posts.find({'author':'Nguyễn Hải Hà'})))