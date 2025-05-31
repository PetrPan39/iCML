from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "EVO API running"}

class PluginInfo(BaseModel):
    name: str
    version: str

@app.post("/register_plugin")
def register_plugin(info: PluginInfo, file: UploadFile):
    return {"msg": f"Plugin {info.name} v{info.version} received"}