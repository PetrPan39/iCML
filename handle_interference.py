plugin_name = "handle_interference"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: handle_interference"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.handle_interference(*args, **kwargs)
