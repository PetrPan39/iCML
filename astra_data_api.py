import httpx
import json
from storage.adapters.base import BaseAdapter

class AstraAdapter(BaseAdapter):
    def __init__(self, endpoint, token, keyspace, table=None):
        self.endpoint = endpoint.rstrip("/")
        self.token = token
        self.keyspace = keyspace
        self.table = table
        self.headers = {
            "Content-Type": "application/json",
            "X-Cassandra-Token": self.token
        }

    def log(self, record):
        if not self.table:
            raise ValueError("Tabulka není nastavena.")
        url = f"{self.endpoint}/api/rest/v2/keyspaces/{self.keyspace}/tables/{self.table}/rows"
        payload = {"columns": record}
        response = httpx.post(url, headers=self.headers, data=json.dumps(payload))
        if response.status_code != 201:
            raise RuntimeError(f"Logování selhalo: {response.status_code} {response.text}")

    def query(self, **filters):
        if not self.table:
            raise ValueError("Tabulka není nastavena.")
        where = " AND ".join([f"{k}='{v}'" for k, v in filters.items()])
        url = f"{self.endpoint}/api/rest/v2/keyspaces/{self.keyspace}/tables/{self.table}/rows?where={where}"
        response = httpx.get(url, headers=self.headers)
        if response.status_code != 200:
            raise RuntimeError(f"Dotaz selhal: {response.status_code} {response.text}")
        return response.json().get("rows", [])

    def rollback(self, version_id):
        raise NotImplementedError("Snapshot rollback není podporován v REST API Astra.")

    def summary(self):
        if not self.table:
            raise ValueError("Tabulka není nastavena.")
        url = f"{self.endpoint}/api/rest/v2/keyspaces/{self.keyspace}/tables/{self.table}/rows"
        response = httpx.get(url, headers=self.headers)
        if response.status_code != 200:
            raise RuntimeError(f"Souhrn selhal: {response.status_code} {response.text}")
        return {"rows": len(response.json().get("rows", []))}


def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
