plugin_name = "summarize"
plugin_description = "Shrne vstupní text pomocí OpenAI GPT."

def run(text=None, **kwargs):
    if not text:
        return {"error": "Chybí vstupní text"}

    from cmlb_modules.summarizer import Summarizer
    summarizer = Summarizer()
    return summarizer.summarize(text)
