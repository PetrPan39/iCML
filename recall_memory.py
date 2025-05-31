plugin_name = "recall_memory"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: recall_memory"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.recall_memory(*args, **kwargs)
