from pymongo import MongoClient

def mongoDB(db, collection=None):
    client = MongoClient('140.112.147.132')
    client.admin.authenticate('achiii', 'gjoKClmg8eQDF4pKeVXMkTnX7wL/9MVilkavArDouNA=')
    if collection:
        output = client[db][collection]
    else:
        output = client[db]
    return output

# This is used for accessing mongodb without authentication
#from pymongo import Connection
#def connect(db, collection):
#       C = Connection(host='localhost', port=27017)
#       output = C[db][collection]
#       C.close()
#       return output
