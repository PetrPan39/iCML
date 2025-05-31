plugin_name = "log"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: log"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.log(*args, **kwargs)
