import importlib.util
import os
import ast

class PluginInfo:
    def __init__(self, name, path, description=None, functions=None, requires=None):
        self.name = name
        self.path = path
        self.description = description or ""
        self.functions = functions or []
        self.requires = requires or []

    def __repr__(self):
        return f"<Plugin {self.name}: {self.description}>"

class PluginManager:
    def __init__(self, plugin_folder="modules/pluginbank"):
        self.plugin_folder = plugin_folder
        self.plugins = {}
        self._scan_plugins()

    def _scan_plugins(self):
        for file in os.listdir(self.plugin_folder):
            if file.endswith(".py") and not file.startswith("_"):
                plugin_path = os.path.join(self.plugin_folder, file)
                name = file[:-3]
                info = self._analyze_plugin(name, plugin_path)
                if info:
                    self.plugins[name] = info

    def _analyze_plugin(self, name, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                source = f.read()
            tree = ast.parse(source)

            docstring = ast.get_docstring(tree)
            functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
            imports = [
                n.names[0].name for n in ast.walk(tree)
                if isinstance(n, ast.Import) or isinstance(n, ast.ImportFrom)
            ]

            return PluginInfo(name, path, docstring, functions, imports)
        except Exception as e:
            print(f"Chyba při analýze pluginu {name}: {e}")
            return None

    def list_plugins(self):
        return list(self.plugins.keys())

    def get_plugin_info(self, name):
        return self.plugins.get(name)

    def load_plugin(self, name):
        if name not in self.plugins:
            raise ValueError(f"Plugin '{name}' nebyl nalezen.")
        plugin_path = self.plugins[name].path
        spec = importlib.util.spec_from_file_location(name, plugin_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
