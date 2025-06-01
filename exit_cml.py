import os
import sys
import importlib
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox, simpledialog

# Načti .env proměnné
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
sys.path.append(os.path.join(os.path.dirname(__file__), "dynamic_modules"))

# Hlavní registry pro moduly a pluginy
module_registry = {}

def understand_and_dispatch(task_text):
    """
    Základní 'inteligence': analyzuje zadání a rozhodne, jaký modul použít nebo vytvořit.
    """
    # Jednoduchý příklad: rozhodování podle klíčových slov (nahraď AI analýzou dle potřeb)
    task = task_text.lower()
    if "evo" in task:
        return get_or_create_module("EvoModule", evo_template)
    elif "vizualizace" in task or "graf" in task:
        return get_or_create_module("VisualizerModule", visualizer_template)
    elif "ai" in task or "chat" in task:
        return get_or_create_module("AIChatModule", aichat_template)
    elif "orchestrator" in task or "koordina" in task:
        return get_or_create_module("OrchestratorModule", orchestrator_template)
    else:
        # Pokud nerozumí, vytvoří obecný modul pro nový úkol
        func_name = "Task_" + str(abs(hash(task_text)))[:8]
        return get_or_create_module(func_name, generic_template, custom_name=task_text)

def get_or_create_module(name, template, custom_name=None):
    """
    Najde nebo vytvoří modul podle jména a šablony.
    """
    if name in module_registry:
        return module_registry[name]
    module_path = os.path.join("dynamic_modules", f"{name}.py")
    if not os.path.exists(module_path):
        with open(module_path, "w", encoding="utf-8") as f:
            f.write(template.format(name=name, custom_name=custom_name or name))
    importlib.invalidate_caches()
    mod = importlib.import_module(name)
    module_registry[name] = mod
    return mod

# --- Šablony pro nové moduly ---
evo_template = """
class {name}:
    def __init__(self):
        self.status = "EVO modul je připraven."
    def run(self):
        return "Spouštím evoluční algoritmus!"
"""

visualizer_template = """
class {name}:
    def __init__(self):
        self.status = "Vizualizace připravena."
    def run(self):
        return "Zobrazím graf nebo vizualizaci!"
"""

aichat_template = """
class {name}:
    def __init__(self):
        self.status = "AI Chat připraven."
    def run(self):
        return "Mluvím s AI!"
"""

orchestrator_template = """
class {name}:
    def __init__(self):
        self.status = "Orchestrátor připraven."
    def run(self):
        return "Koordinuji činnost všech modulů!"
"""

generic_template = """
class {name}:
    def __init__(self):
        self.status = "Modul '{custom_name}' byl vytvořen na základě zadání."
    def run(self):
        return "Zpracovávám: {custom_name}"
"""

# --- Hlavní GUI/kontrolní panel ---
class SmartCMLPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CML/EVO Inteligentní Řídící Pult")
        self.geometry("860x560")
        self.configure(bg="#262F38")

        tk.Label(self, text="Centrální zadání (napiš, co chceš):", bg="#262F38", fg="#ffffff", font=("Segoe UI", 13)).pack(pady=6)
        self.input_box = tk.Entry(self, font=("Segoe UI", 13), width=60)
        self.input_box.pack(pady=6)
        self.input_box.bind("<Return>", self.process_task)

        self.result_box = tk.Text(self, height=20, width=95, bg="#212935", fg="#a7e7ff", font=("Consolas", 11))
        self.result_box.pack(padx=10, pady=8)
        self.result_box.config(state='disabled')

        self.status_var = tk.StringVar(value="Připraveno.")
        tk.Label(self, textvariable=self.status_var, bg="#18202b", fg="#b1c2d8", font=("Segoe UI", 11)).pack(fill=tk.X, side=tk.BOTTOM)

    def process_task(self, event=None):
        task = self.input_box.get().strip()
        self.input_box.delete(0, tk.END)
        if not task:
            return
        self.append_result(f"> {task}")
        mod = understand_and_dispatch(task)
        self.append_result(f"Použit modul: {mod.__name__}")
        try:
            instance = getattr(mod, mod.__name__)()
            result = instance.run()
            self.append_result(f"[Výsledek]: {result}")
            self.status_var.set(instance.status)
        except Exception as e:
            self.append_result(f"[Chyba]: {e}")
            self.status_var.set("Chyba při zpracování.")

    def append_result(self, msg):
        self.result_box.config(state='normal')
        self.result_box.insert(tk.END, msg + "\n")
        self.result_box.see(tk.END)
        self.result_box.config(state='disabled')

if __name__ == "__main__":
    if not os.path.exists("dynamic_modules"):
        os.makedirs("dynamic_modules")
    SmartCMLPanel().mainloop()