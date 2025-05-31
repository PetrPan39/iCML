from dotenv import load_dotenv
load_dotenv()

import uvicorn
from api_server import app

if __name__ == "__main__":
    uvicorn.run("api_server:app", host="0.0.0.0", port=8080, reload=True)

def run(*args, **kwargs):
    return 'run() placeholder - not yet implemented'
