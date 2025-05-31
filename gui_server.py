from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from openai_client import OpenAIClient

app = FastAPI()
client = OpenAIClient()

app.mount("/gui", StaticFiles(directory="gui", html=True), name="gui")

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("gui/index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    response = client.ask(prompt)
    return JSONResponse(content={"response": response})

def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
