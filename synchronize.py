plugin_name = "synchronize"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: synchronize"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.synchronize(*args, **kwargs)
