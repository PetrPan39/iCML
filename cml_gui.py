import tkinter as tk
from main_cml_orchestrator import CML_CentralOrchestrator

class App:
    def __init__(self, root):
        self.orch = CML_CentralOrchestrator()
        self.root = root
        self.root.title("CML EVO GUI")

        self.text = tk.Text(root, height=20, width=80)
        self.text.pack()

        self.start_btn = tk.Button(root, text="Start EVO", command=self.start_evo)
        self.start_btn.pack()

        self.step_btn = tk.Button(root, text="Krok EVO", command=self.step_evo)
        self.step_btn.pack()

    def start_evo(self):
        res = self.orch.start_evo(8)
        self.text.insert(tk.END, res + "\n")

    def step_evo(self):
        res = self.orch.step_evo()
        self.text.insert(tk.END, res + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()