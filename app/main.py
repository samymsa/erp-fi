import json

from fastapi import FastAPI

from .routers import ca

app = FastAPI()


app.include_router(ca.router)


@app.get("/meuch_map")
async def meuch_map():
    with open("app/meuch_map.json") as f:
        data = json.load(f)

    return data
