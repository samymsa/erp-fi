from datetime import date

from fastapi import APIRouter
from pydantic import BaseModel

from app.services import va

router = APIRouter(
    prefix="/tva",
)


class TVAResponse(BaseModel):
    tva: float


@router.get(
    "",
    description="Calculer la TVA à déclarer sur une période donnée",
    response_model=TVAResponse,
)
async def tva(debut: date = date.min, fin: date = date.max):
    tx_tva = 0.2
    total_ventes = sum(vente["total"] for vente in va.ventes(debut, fin))
    total_achats = sum(achat["total"] for achat in va.achats(debut, fin))
    return {"tva": (total_ventes - total_achats) * tx_tva}
