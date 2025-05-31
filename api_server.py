"""
Plugin: Api Server
Opravený a standardizovaný plugin napojený na CML_B
"""

plugin_name = "api_server"
plugin_description = "Standardizovaný plugin automaticky opravený ze souboru api_server.py"

def run(*args, **kwargs):
    from CML_B import EvolucniOptimalizace
    evo = EvolucniOptimalizace()
    if hasattr(evo, "api_server"):
        return getattr(evo, "api_server")(*args, **kwargs)
    return f"Plugin handler 'api_server' neexistuje v CML_B."
