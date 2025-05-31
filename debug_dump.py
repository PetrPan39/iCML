plugin_name = "debug_dump"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: debug_dump"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.debug_dump(*args, **kwargs)
