plugin_name = "run_plugins"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: run_plugins"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.run_plugins(*args, **kwargs)
