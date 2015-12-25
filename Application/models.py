import pymongo
from couchbase.exceptions import CouchbaseError
from couchbase.n1ql import N1QLQuery
from couchbase.bucket import Bucket
from pymongo.errors import PyMongoError
from cassandra.cluster import Cluster
from cassandra.connection import ErrorMessage


class CouchDBSession:
    c = Bucket('couchbase://localhost/FHT')

    @classmethod
    def exec_query(self, query_string):
        res = []
        try:
            q = N1QLQuery(query_string)
            for row in self.c.n1ql_query(q):
                res.append("Data:")
                res.append(row)
        except CouchbaseError as e:
            res.append("Error: {"+e.message+"}")
        return res

class MongoDBSession:
    client = pymongo.MongoClient("localhost", 27017)
    db = client.FHT
    students = db['students']

    @classmethod
    def exec_query(self, query_string):
        res = []
        try:
            res = eval('list(self.'+query_string+')')
        except PyMongoError as e:
            res.append("Couldn't retrieve value for key "+e.message)
        return res

class CassandraDBSession:
    cluster = Cluster()
    session = cluster.connect('mykeyspace')

    @classmethod
    def exec_query(self, query_string):
        res = []
        try:
            for row in self.session.execute(query_string):
                res.append(row)
        except ErrorMessage as e:
            res.append("Couldn't retrieve value for key "+e.message)
        return res