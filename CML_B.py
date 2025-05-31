import importlib
import os

class CML_B:
    def __init__(self, plugins_path="plugins"):
        self.plugins = []
        self._load_plugins(plugins_path)
    
    def _load_plugins(self, plugins_path):
        # Importuje modul plugins i bez .py přípony
        plugins_file = os.path.abspath(plugins_path)
        if not os.path.exists(plugins_file) and os.path.exists(plugins_file + ".py"):
            plugins_file = plugins_file + ".py"
        spec = importlib.util.spec_from_file_location("plugins", plugins_file)
        plugins_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugins_mod)
        for name in dir(plugins_mod):
            item = getattr(plugins_mod, name)
            if callable(item) and hasattr(item, "typ") and hasattr(item, "funkce"):
                self.plugins.append({
                    "name": name,
                    "typ": item.typ,
                    "funkce": item.funkce,
                    "callable": item
                })

    def list_types(self):
        return sorted(set(p["typ"] for p in self.plugins))

    def list_functions(self, typ=None):
        if typ:
            return [p["funkce"] for p in self.plugins if p["typ"] == typ]
        return [p["funkce"] for p in self.plugins]

    def get_plugin(self, typ, funkce):
        for p in self.plugins:
            if p["typ"] == typ and p["funkce"] == funkce:
                return p["callable"]
        return None

    def call(self, typ, funkce, *args, **kwargs):
        plugin = self.get_plugin(typ, funkce)
        if plugin:
            return plugin(*args, **kwargs)
        raise ValueError(f"Plugin {typ}/{funkce} nenalezen!")