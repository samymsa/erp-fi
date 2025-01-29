from datetime import date

from fastapi import APIRouter
from pydantic import BaseModel

from app.services import va

router = APIRouter(
    prefix="/ca",
)


class CAResponse(BaseModel):
    ca: float


@router.get(
    "",
    description="Récupérer le chiffre d'affaires sur une période donnée",
    response_model=CAResponse,
)
async def ca(debut: date = date.min, fin: date = date.max) -> dict:
    ventes = va.ventes(debut, fin)
    ca = sum(vente["total"] for vente in ventes)
    return {"ca": ca}
