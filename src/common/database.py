import pymongo


class Database:
    _URI = os.environ.get('DB_URI')
    _DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database._URI)
        Database._DATABASE = client["tsp"]

    @staticmethod
    def insert(collection, data):
        Database._DATABASE[collection].insert(data)

    @staticmethod
    def delete(collection, query):
        Database._DATABASE[collection].remove(query)

    @staticmethod
    def find(collection, query):
        return Database._DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database._DATABASE[collection].find_one(query)

    @staticmethod
    def count(collection, query):
        return Database._DATABASE[collection].count(query)

    @staticmethod
    def update(collection, query, data):
        Database._DATABASE[collection].update(query, data, upsert=True)

