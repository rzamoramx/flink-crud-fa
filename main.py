
from fastapi import FastAPI
from symbols.adapters.api.rest.v1 import router as router_v1
import uvicorn

app = FastAPI()

# Routes
app.include_router(router_v1, prefix="/v1")


@app.get("/ping")
def index():
    return "ok"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
