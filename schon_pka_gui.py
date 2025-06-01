
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from scipy.linalg import expm, hessenberg, norm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

hbar = 1.0545718e-34  # Planckova konstanta (redukovaná) v J·s

def kvantova_predikce(H, psi_0, delta_t_fs):
    H_joule = H * 1e-19
    delta_t_real = delta_t_fs * 1e-15

    U_full = expm(-1j * H_joule * delta_t_real / hbar)
    psi_full = U_full @ psi_0

    H_hess, Q = hessenberg(H_joule, calc_q=True)
    U_hess = Q @ expm(-1j * H_hess * delta_t_real / hbar) @ Q.T
    psi_hess = U_hess @ psi_0

    diff = norm(psi_full - psi_hess)
    return psi_full, psi_hess, diff

class KvantoveGUI:
    def __init__(self, root):
        self.root = root
        root.title("Schőn PKA – Kvantová predikce")

        ttk.Label(root, text="Časový krok (fs):").grid(row=0, column=0, sticky="w")
        self.delta_t_entry = ttk.Entry(root)
        self.delta_t_entry.insert(0, "1.0")
        self.delta_t_entry.grid(row=0, column=1, sticky="ew")

        ttk.Button(root, text="Spustit výpočet", command=self.spustit_vypocet).grid(row=1, column=0, columnspan=2)

        self.text = tk.Text(root, height=20, width=80, bg="black", fg="white", font=("Courier", 10))
        self.text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, root)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)

    def vypis_na_tabuli(self, text):
        self.text.insert(tk.END, text + "\n")
        self.text.see(tk.END)

    def spustit_vypocet(self):
        self.text.delete('1.0', tk.END)
        try:
            delta_t_fs = float(self.delta_t_entry.get())
        except ValueError:
            self.vypis_na_tabuli("⚠️ Neplatná hodnota časového kroku.")
            return

        H = np.array([[1.0, 0.5, 0.0, 0.0],
                      [0.5, 1.0, 0.5, 0.0],
                      [0.0, 0.5, 1.0, 0.5],
                      [0.0, 0.0, 0.5, 1.0]])
        psi_0 = np.array([1.0, 0.0, 0.0, 0.0])

        self.vypis_na_tabuli("🔢 Spouštím výpočet...")
        psi_full, psi_hess, rozdil = kvantova_predikce(H, psi_0, delta_t_fs)

        self.vypis_na_tabuli("📘 Výsledný stav (plná simulace):")
        for val in psi_full:
            self.vypis_na_tabuli(f"  {val:.5f}")

        self.vypis_na_tabuli("\n📗 Výsledný stav (Schőn PKA):")
        for val in psi_hess:
            self.vypis_na_tabuli(f"  {val:.5f}")

        self.vypis_na_tabuli(f"\n📏 Rozdíl mezi metodami: {rozdil:.3e}")

        self.ax.clear()
        self.ax.plot(np.real(psi_full), label="Re(Plná simulace)", marker='o')
        self.ax.plot(np.real(psi_hess), label="Re(Schőn PKA)", linestyle='--', marker='x')
        self.ax.set_title("Porovnání reálných částí kvantového stavu")
        self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = KvantoveGUI(root)
    root.mainloop()
