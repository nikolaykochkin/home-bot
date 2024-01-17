import uvicorn
import logging
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from config import server_config

logger = logging.getLogger(__name__)

app = FastAPI()

instrumentator = Instrumentator()

instrumentator.instrument(app)
instrumentator.expose(app)

config = uvicorn.Config(app, **server_config)
server = uvicorn.Server(config)


@app.get("/health")
async def health():
    return {"status": "UP"}
