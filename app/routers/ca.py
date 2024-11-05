import decimal

from fastapi import APIRouter
from pydantic import BaseModel, PositiveInt

router = APIRouter(
    prefix="/ca",
)


class Vente(BaseModel):
    prix_unitaire: decimal.Decimal
    quantite: PositiveInt


@router.post("/")
async def ca(ventes: list[Vente]):
    """Calcul du chiffre d'affaires"""
    return {
        "chiffres_affaires_total": sum(
            [vente.prix_unitaire * vente.quantite for vente in ventes]
        )
    }
