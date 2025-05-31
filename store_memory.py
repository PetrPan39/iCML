plugin_name = "store_memory"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: store_memory"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.store_memory(*args, **kwargs)
