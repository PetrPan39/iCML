from storage.adapters.base import BaseAdapter

class MemoryStorage:
    def __init__(self, adapter: BaseAdapter):
        self.adapter = adapter
        self.cache = {}
        
    def __init__(self, adapter):
        self.adapter = adapter

    def save(self, data):
        if self.adapter:
            self.adapter.save(data)

    def load(self):
        if self.adapter:
            return self.adapter.load()
        return None

    def log(self, data):  # 🔧 přidaná metoda
        self.save(data)
    def create(self, key, value):
        self.cache[key] = value
        try:
            self.adapter.log({"key": key, "value": value})
        except Exception as e:
            print(f"[MemoryStorage] Chyba logování do adaptéru: {e}")

    def retrieve(self, key):
        if key in self.cache:
            return self.cache[key]
        try:
            result = self.adapter.query(key=key)
            if result:
                self.cache[key] = result[0].get("value", None)
                return self.cache[key]
        except Exception as e:
            print(f"[MemoryStorage] Chyba při načítání z adaptéru: {e}")
        return None

    def exists(self, key):
        return key in self.cache or self.retrieve(key) is not None


def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
