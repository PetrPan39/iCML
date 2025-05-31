plugin_name = "add_decision"
plugin_description = "Rozhodovací modul pro zpracování dotazů."

def run(question=None, **kwargs):
    if not question:
        return {"error": "Chybí vstupní otázka"}

    from cmlb_modules.decision_engine import DecisionEngine
    engine = DecisionEngine()
    return engine.add_decision({"question": question})
