class DecisionStorage:
    def __init__(self, adapter):
        self.adapter = adapter

    def save_decision(self, data):
        if self.adapter:
            self.adapter.save(data)

    def load_decision(self):
        if self.adapter:
            return self.adapter.load()
        return None


def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
