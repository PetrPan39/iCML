plugin_name = "add_expression"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: add_expression"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.add_expression(*args, **kwargs)
