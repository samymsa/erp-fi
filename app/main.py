from fastapi import FastAPI
from fastapi.routing import APIRoute


from .routers import ca, rentabilite_projet, tva

app = FastAPI()

routers = [ca.router, tva.router, rentabilite_projet.router]


for router in routers:
    app.include_router(router)


def get_route_info(route: APIRoute):
    method = next(iter(route.methods))
    key = f"FI_{method}_{route.endpoint.__name__.upper()}"
    query_params = [param.name for param in route.dependant.query_params]
    response = (
        route.response_model.model_json_schema() if route.response_model else None
    )

    return {
        "key": key,
        "endpoint": route.path,
        "description": route.description,
        "type": method,
        "routeFormat": None,
        "queryParams": query_params,
        "body": None,
        "response": response,
    }


@app.get("/meuch_map")
async def meuch_map():
    return [get_route_info(route) for router in routers for route in router.routes]
