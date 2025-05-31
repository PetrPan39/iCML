# modules/telemetry/telemetry_storage
from modules.base import EvoModule

class TelemetryStorage(EvoModule):
    def init(self, core):
        super().init(core)
        self.adapter = core.db

    def log_event(self, event: dict):
        self.adapter.insert(event)


def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
