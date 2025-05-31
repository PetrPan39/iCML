from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from storage.adapters.base import BaseAdapter

class AstraAdapter(BaseAdapter):
    def __init__(self, keyspace, table, user, password, secure_connect_bundle):
        auth = PlainTextAuthProvider(username=user, password=password)
        self.cluster = Cluster([secure_connect_bundle], auth_provider=auth)
        self.session = self.cluster.connect(keyspace)
        self.table = table

    def log(self, record):
        cols = ", ".join(record.keys())
        vals = ", ".join([f"%({k})s" for k in record])
        q = f"INSERT INTO {self.table} ({cols}) VALUES ({vals})"
        self.session.execute(q, record)

    def query(self, **filters):
        conditions = " AND ".join([f"{k}=%({k})s" for k in filters])
        q = f"SELECT * FROM {self.table} WHERE {conditions}"
        return list(self.session.execute(q, filters))

    def rollback(self, version_id):
        self.session.execute(f"CALL snapshot_rollback('{self.table}', '{version_id}')")

    def summary(self):
        return list(self.session.execute(f"SELECT COUNT(*) FROM {self.table}"))[0]


def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
