import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://Donner:DonnerPass1@cluster0-yz8ix.mongodb.net/test?retryWrites=true&ssl_cert_reqs=CERT_NONE")

print(myclient.list_database_names())

db_list = myclient.list_database_names()
curr_db = myclient['examples']
cluster = curr_db.inventory

# print inventory db
for i in cluster.find():
    print(i)

print('\n\n')

# print all item names from inventory
for i in cluster.find():
    print(i['item'])

print('\n\n')

# print all item quantities from inventory
for i in cluster.find():
    print(i['qty'])

print('\n\n')

# find all items with unit of measure in cm and print only the item name
# duplicate items in db exist so may see duplicate stats but they have different Obj Ids
for i in cluster.find({'item': {'$eq': 'planner'}}):
    print(i)

print('\n\n')

# insert TP - So far we have not covered it Mongo does duplicate checking
cluster.insert_one({'item': 'toilet paper', 'qty' : -100, 'status' : 'F', 'tags' : ['white']})

for i in cluster.find():
    print(i)