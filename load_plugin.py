plugin_name = "load_plugin"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: load_plugin"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.load_plugin(*args, **kwargs)
