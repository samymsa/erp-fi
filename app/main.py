import json

from fastapi import FastAPI

from .routers import ca, rentabilite_projet, tva

app = FastAPI()

app.include_router(ca.router)
app.include_router(tva.router)
app.include_router(rentabilite_projet.router)


@app.get("/meuch_map")
async def meuch_map():
    with open("app/meuch_map.json") as f:
        data = json.load(f)

    return data
