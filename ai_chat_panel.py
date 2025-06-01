import tkinter as tk

class AIChatPanel(tk.Frame):
    def __init__(self, master, use_openai=True, **kwargs):
        super().__init__(master, **kwargs)
        self.use_openai = tk.BooleanVar(value=use_openai)
        self.create_widgets()

    def create_widgets(self):
        # Přepínač OpenAI/Interní engine
        switch = tk.Checkbutton(
            self,
            text="Použít OpenAI ChatGPT",
            variable=self.use_openai,
            onvalue=True,
            offvalue=False,
            font=("Segoe UI", 12),
            command=self.on_switch
        )
        switch.grid(row=0, column=0, sticky="w", padx=12, pady=6)

        # Textová pole pro chat
        self.entry = tk.Entry(self, width=60, font=("Segoe UI", 12))
        self.entry.grid(row=1, column=0, padx=12, pady=4)
        self.entry.bind("<Return>", self.process_input)

        self.output = tk.Text(self, height=10, width=70, font=("Consolas", 11), state='disabled')
        self.output.grid(row=2, column=0, padx=12, pady=8)

    def on_switch(self):
        # Můžeš přidat logiku pro zobrazení stavu/varování atd.
        if self.use_openai.get():
            self.log_output("[INFO] OpenAI/ChatGPT je aktivní.")
        else:
            self.log_output("[INFO] Komunikace pouze z vektorové matrice.")

    def process_input(self, event=None):
        user_text = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        if not user_text:
            return

        if self.use_openai.get():
            # ZDE: dotaz na OpenAI/ChatGPT + případně vektorová paměť
            response = self.ask_openai(user_text)
        else:
            # ZDE: odpověď pouze z vektorové matrice
            response = self.ask_internal_engine(user_text)

        self.log_output(f"Já: {user_text}\nAI: {response}\n")

    def ask_openai(self, text):
        # Skutečné volání na OpenAI zde
        return "[OpenAI odpověď zde]"

    def ask_internal_engine(self, text):
        # Skutečná odpověď pouze z vektorové matrice zde
        return "[Odpověď pouze z vektorové matrice zde]"

    def log_output(self, msg):
        self.output.config(state='normal')
        self.output.insert(tk.END, msg + "\n")
        self.output.see(tk.END)
        self.output.config(state='disabled')