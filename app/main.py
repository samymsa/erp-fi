from inspect import isclass

from fastapi import Depends, FastAPI
from fastapi.routing import APIRoute
from pydantic import BaseModel

from app.dependencies import get_integration_service
from app.routers import compte_resultat
from app.services.integration_service import IntegrationService

from .routers import ca, rentabilite_projet, tva

app = FastAPI()

routers = [ca.router, tva.router, rentabilite_projet.router, compte_resultat.router]


for router in routers:
    app.include_router(router)


def get_route_info(route: APIRoute):
    method = next(iter(route.methods))
    key = f"FI_{method}_{route.endpoint.__name__.upper()}"
    query_params = [param.name for param in route.dependant.query_params]
    response = get_route_response_schema(route)

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


def get_route_response_schema(route: APIRoute):
    if not route.response_model:
        return None

    if isclass(route.response_model) and issubclass(route.response_model, BaseModel):
        return route.response_model.model_json_schema()

    return route.response_model.__name__


@app.get("/meuch_map")
async def meuch_map():
    return [get_route_info(route) for router in routers for route in router.routes]


@app.get("/register")
async def register(
    integration_service: IntegrationService = Depends(get_integration_service),
):
    return await integration_service.register()
