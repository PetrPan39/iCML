__znacka__ = 'submit_frequency'
__description__ = 'TODO: Add description here'


import tkinter as tk
from tkinter import messagebox
import httpx

def submit_frequency():
    """
    Odesílá frekvenci na API pro výpočet Planckovy energie.
    """
    frequency = float(frequency_entry.get())
    response = httpx.post("http://127.0.0.1:5000/calculate_planck_energy", json={"frequency": frequency})
    result = response.json()
    messagebox.showinfo("Výsledek", f"Energie fotonu: {result.get('energy')} J")

def submit_heisenberg():
    """
    Odesílá data na API pro ověření Heisenbergova principu.
    """
    position = float(position_entry.get())
    momentum = float(momentum_entry.get())
    response = httpx.post("http://127.0.0.1:5000/check_heisenberg", json={
        "position_uncertainty": position,
        "momentum_uncertainty": momentum
    })
    result = response.json()
    satisfied = result.get("heisenberg_satisfied")
    message = "Heisenbergův princip je splněn" if satisfied else "Heisenbergův princip není splněn"
    messagebox.showinfo("Výsledek", message)

# GUI
root = tk.Tk()
root.title("Fyzikální výpočty")

tk.Label(root, text="Frekvence (Hz):").grid(row=0, column=0)
frequency_entry = tk.Entry(root)
frequency_entry.grid(row=0, column=1)
tk.Button(root, text="Vypočítat Planckovu energii", command=submit_frequency).grid(row=0, column=2)

tk.Label(root, text="Nejistota polohy (m):").grid(row=1, column=0)
position_entry = tk.Entry(root)
position_entry.grid(row=1, column=1)

tk.Label(root, text="Nejistota hybnosti (kg·m/s):").grid(row=2, column=0)
momentum_entry = tk.Entry(root)
momentum_entry.grid(row=2, column=1)
tk.Button(root, text="Zkontrolovat Heisenberga", command=submit_heisenberg).grid(row=2, column=2)

root.mainloop()


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'

def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
