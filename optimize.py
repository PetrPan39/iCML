plugin_name = "optimize"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: optimize"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.optimize(*args, **kwargs)
