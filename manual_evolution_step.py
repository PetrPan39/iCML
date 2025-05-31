plugin_name = "manual_evolution_step"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: manual_evolution_step"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.manual_evolution_step(*args, **kwargs)
