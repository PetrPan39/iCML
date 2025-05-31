plugin_name = "add_emotion"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: add_emotion"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.add_emotion(*args, **kwargs)
