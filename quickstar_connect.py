"""
Plugin: Quickstar Connect
Opravený a standardizovaný plugin napojený na CML_B
"""

plugin_name = "quickstar_connect"
plugin_description = "Standardizovaný plugin automaticky opravený ze souboru quickstar_connect.py"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    if hasattr(evo, "quickstar_connect"):
        return getattr(evo, "quickstar_connect")(*args, **kwargs)
    return f"Plugin handler 'quickstar_connect' neexistuje v CML_B."
