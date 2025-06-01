import numpy as np
import tkinter as tk
from tkinter import ttk
from scipy.linalg import expm, hessenberg, norm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

hbar = 1.0545718e-34  # Planckova konstanta

# Prediktivni vypocet podle Schőn PKA
def schon_pka_prediction(H, psi_0, delta_t_fs):
    H_joule = H * 1e-19
    delta_t_real = delta_t_fs * 1e-15

    H_hess, Q = hessenberg(H_joule, calc_q=True)
    U_hess = Q @ expm(-1j * H_hess * delta_t_real / hbar) @ Q.T
    psi_pred = U_hess @ psi_0

    return psi_pred, H_hess

# Kontrolni vypocet klasicky
def full_simulation(H, psi_0, delta_t_fs):
    H_joule = H * 1e-19
    delta_t_real = delta_t_fs * 1e-15
    U_full = expm(-1j * H_joule * delta_t_real / hbar)
    psi_full = U_full @ psi_0
    return psi_full

# GUI aplikace
class SchonPKAGUI:
    def __init__(self, root):
        self.root = root
        root.title("Schőn PKA: Prediktivní Kvantový Výpočet")

        # Promenne
        self.entries = {}
        for i, label in enumerate(["H00", "H01", "H11", "\u03c8_0[0]", "\u03c8_0[1]", "\u0394t (fs)"]):
            ttk.Label(root, text=label).grid(row=i, column=0, sticky="w")
            entry = ttk.Entry(root)
            entry.grid(row=i, column=1, sticky="ew")
            self.entries[label] = entry

        self.calc_btn = ttk.Button(root, text="Spustit predikci", command=self.spustit_predikci)
        self.calc_btn.grid(row=6, column=0, columnspan=2, pady=10)

        self.result_var = tk.StringVar()
        ttk.Label(root, textvariable=self.result_var).grid(row=7, column=0, columnspan=2)

        self.compare_btn = ttk.Button(root, text="Spustit kontrolní výpočet", command=self.spustit_kontrolu)
        self.compare_btn.grid(row=8, column=0, columnspan=2, pady=5)

        self.result2_var = tk.StringVar()
        ttk.Label(root, textvariable=self.result2_var).grid(row=9, column=0, columnspan=2)

        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.grid(row=10, column=0, columnspan=2)

        self.figure, self.ax = plt.subplots(figsize=(5, 3))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack()

    def spustit_predikci(self):
        H = np.array([[float(self.entries["H00"].get()), float(self.entries["H01"].get())],
                      [float(self.entries["H01"].get()), float(self.entries["H11"].get())]])
        psi_0 = np.array([float(self.entries["\u03c8_0[0]"].get()), float(self.entries["\u03c8_0[1]"].get())])
        delta_t_fs = float(self.entries["\u0394t (fs)"].get())

        self.psi_pred, self.H_hess = schon_pka_prediction(H, psi_0, delta_t_fs)
        self.result_var.set(f"Predikce (Schőn PKA): {np.round(self.psi_pred, 5)}")
        self.ax.clear()
        self.ax.plot(np.real(self.psi_pred), label="Re(PKA)", marker='o')
        self.ax.set_title("Reálná část predikce")
        self.ax.legend()
        self.canvas.draw()

    def spustit_kontrolu(self):
        H = np.array([[float(self.entries["H00"].get()), float(self.entries["H01"].get())],
                      [float(self.entries["H01"].get()), float(self.entries["H11"].get())]])
        psi_0 = np.array([float(self.entries["\u03c8_0[0]"].get()), float(self.entries["\u03c8_0[1]"].get())])
        delta_t_fs = float(self.entries["\u0394t (fs)"].get())

        psi_full = full_simulation(H, psi_0, delta_t_fs)
        diff = norm(self.psi_pred - psi_full)
        self.result2_var.set(f"Kontrola: {np.round(psi_full, 5)}\nRozdíl: {diff:.2e}")
        self.ax.plot(np.real(psi_full), label="Re(Kontrola)", linestyle='--', marker='x')
        self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = SchonPKAGUI(root)
    root.mainloop()
