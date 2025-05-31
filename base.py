class BaseStorage:
    """Abstraktní základ pro storage moduly (rozhraní)."""
    def __init__(self, adapter):
        self.adapter = adapter

    def log(self, record):
        return self.adapter.log(record)

    def query(self, **filters):
        return self.adapter.query(**filters)

    def rollback(self, version_id):
        return self.adapter.rollback(version_id)

    def summary(self):
        return self.adapter.summary()

class BaseAdapter:
    """Rozhraní adapteru pro perzistenci."""
    def log(self, record):
        raise NotImplementedError

    def query(self, **filters):
        raise NotImplementedError

    def rollback(self, version_id):
        raise NotImplementedError

    def summary(self):
        raise NotImplementedError


def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
