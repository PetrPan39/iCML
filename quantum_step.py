plugin_name = "quantum_step"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: quantum_step"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.quantum_step(*args, **kwargs)
