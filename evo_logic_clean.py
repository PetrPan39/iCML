"""
Plugin: Evo Logic Clean
Opravený a standardizovaný plugin napojený na CML_B
"""

plugin_name = "evo_logic_clean"
plugin_description = "Standardizovaný plugin automaticky opravený ze souboru evo_logic_clean.py"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    if hasattr(evo, "evo_logic_clean"):
        return getattr(evo, "evo_logic_clean")(*args, **kwargs)
    return f"Plugin handler 'evo_logic_clean' neexistuje v CML_B."
