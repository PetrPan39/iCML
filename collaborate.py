plugin_name = "collaborate"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: collaborate"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.collaborate(*args, **kwargs)
