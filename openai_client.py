import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIClient:
    def __init__(self, model="gpt-4", system_prompt="Jsi pomocná jednotka systému EVO."):
        self.model = model
        self.system_prompt = {"role": "system", "content": system_prompt}
        self.history = []

    def ask(self, user_input, functions=None):
        messages = [self.system_prompt] + self.history + [{"role": "user", "content": user_input}]
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                functions=functions or None,
                function_call="auto" if functions else None,
                temperature=0.7
            )
            message = response["choices"][0]["message"]
            self.history.append({"role": "user", "content": user_input})
            self.history.append(message)
            return message.get("content", "Žádná odpověď")
        except Exception as e:
            return f"Chyba OpenAI: {e}"

    def reset_history(self):
        self.history = []

def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
