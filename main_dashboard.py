import tkinter as tk
from tkinter import ttk
import threading
import os
from dotenv import load_dotenv

# OpenAI podpora (nové API!)
try:
    import openai
except ImportError:
    openai = None

# Načti klíč z .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Pokud OpenAI je dostupné, inicializuj klienta dle nové verze openai>=1.0.0
if openai and OPENAI_API_KEY:
    openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)
else:
    openai_client = None

class EvoGPTGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CML/EVO GUI (EVO / GPT přepínač)")
        self.geometry("700x500")
        self.configure(bg="#242b34")
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        # Rámec pro nastavení
        settings_frame = tk.Frame(self, bg="#242b34")
        settings_frame.pack(fill="x", padx=10, pady=5)

        # Přepínač EVO/GPT
        self.use_gpt = tk.BooleanVar(value=True)
        gpt_check = ttk.Checkbutton(
            settings_frame,
            text="Použít OpenAI GPT odpověď",
            variable=self.use_gpt,
            onvalue=True,
            offvalue=False
        )
        gpt_check.pack(side="left", padx=5)
        self.status_var = tk.StringVar(value="Připraveno.")
        status_label = tk.Label(settings_frame, textvariable=self.status_var, fg="#b0ffb7", bg="#242b34", font=("Segoe UI", 10))
        status_label.pack(side="right", padx=5)

        # Dialogové pole
        self.dialog = tk.Text(self, wrap="word", height=20, bg="#222733", fg="#c9e5f3", font=("Consolas", 11))
        self.dialog.pack(fill="both", expand=True, padx=10, pady=5)
        self.dialog.config(state='disabled')

        # Zadávací pole + tlačítko
        input_frame = tk.Frame(self, bg="#242b34")
        input_frame.pack(fill="x", padx=10, pady=(0,12))
        self.input_entry = tk.Entry(input_frame, font=("Segoe UI", 12))
        self.input_entry.pack(side="left", fill="x", expand=True, padx=(0,6), pady=2)
        self.input_entry.bind("<Return>", self.on_enter)
        send_btn = ttk.Button(input_frame, text="Odeslat", command=self.on_send)
        send_btn.pack(side="right")

    def on_enter(self, event):
        self.on_send()

    def on_send(self):
        user_text = self.input_entry.get().strip()
        if not user_text:
            self.status_var.set("Zadejte text…")
            return
        self.append_dialog(f"Vy: {user_text}")
        self.input_entry.delete(0, tk.END)
        self.status_var.set("Čekám na odpověď...")
        threading.Thread(target=self.get_response, args=(user_text,), daemon=True).start()

    def get_response(self, user_text):
        if self.use_gpt.get():
            response = self.get_gpt_response(user_text)
        else:
            response = self.evo_response(user_text)
        self.append_dialog(f"EVO/GPT: {response}")
        self.status_var.set("Připraveno.")

    def get_gpt_response(self, user_text):
        if not openai_client:
            return "[Chyba] OpenAI není k dispozici nebo chybí klíč."
        try:
            completion = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_text}]
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            return f"[Chyba OpenAI]: {e}"

    def evo_response(self, user_text):
        # Zde nahraď reálnou logikou
        return f"[EVO odpověď] (simulace): Vaše zadání bylo '{user_text}'."

    def append_dialog(self, msg):
        self.dialog.config(state='normal')
        self.dialog.insert(tk.END, msg + "\n")
        self.dialog.see(tk.END)
        self.dialog.config(state='disabled')

    def on_close(self):
        self.destroy()

if __name__ == "__main__":
    EvoGPTGui().mainloop()