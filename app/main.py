from fastapi import FastAPI

from .routers import ca

app = FastAPI()


app.include_router(ca.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
