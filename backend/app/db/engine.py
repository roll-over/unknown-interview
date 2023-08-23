from mongoengine import connect

MONGODB_CONNECTION = connect(db='unknown_mongo', host='mongodb://root:example@unknown_mongo:27017/')
