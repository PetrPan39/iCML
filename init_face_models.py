plugin_name = "init_face_models"
plugin_description = "Automaticky vygenerovaný plugin z EvolucniOptimalizace: init_face_models"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    return evo.init_face_models(*args, **kwargs)
