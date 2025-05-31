plugin_name = "calculator"
plugin_description = "Výpočetní plugin - součet čísel."

def run(numbers=None, **kwargs):
    if not isinstance(numbers, list):
        return {"error": "Zadej seznam čísel jako 'numbers'"}

    from cmlb_modules.toolkit import ToolKit
    toolkit = ToolKit()
    return toolkit.calculate_sum(numbers)
