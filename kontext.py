# core/context.py

from core.CML_A import CML

class CMLContext:
    def __init__(self, n=8):
        self.core = CML(n=n)
        self.tools = ToolRegistry()
        # ihned zaregistrujeme hlavní evoluční modul
        self.tools.register('core', self.core)
