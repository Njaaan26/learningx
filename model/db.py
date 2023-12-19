from . import *

USERNAME = os.getenv("DATABASE_USERNAME")
PASSWORD = os.getenv("DATABASE_PASSWORD")
cluster = MongoClient(
    f'mongodb://{USERNAME}:{PASSWORD}@ac-p2eru3r-shard-00-00.tjckrzw.mongodb.net:27017,ac-p2eru3r-shard-00-01.tjckrzw.mongodb.net:27017,ac-p2eru3r-shard-00-02.tjckrzw.mongodb.net:27017/?ssl=true&replicaSet=atlas-8r06d2-shard-0&authSource=admin&retryWrites=true&w=majority')

db = cluster["sukakita"]

try:
    cluster.admin.command('ping')
    print("You successfully connected to MongoDB!")
except Exception as e:
    print(e)
