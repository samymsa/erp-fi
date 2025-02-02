from datetime import date

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_va_service
from app.services.va_service import VAService

router = APIRouter(
    prefix="/compte_resultat",
)


class CompteResultatResponse(BaseModel):
    charges: float
    produits: float
    resultat: float


@router.get(
    "",
    description="Récupérer le compte de résultat sur une période donnée",
    response_model=CompteResultatResponse,
)
async def compte_de_resultat_a_date(
    start_date: date = date.min,
    end_date: date = date.max,
    va_service: VAService = Depends(get_va_service),
) -> dict:
    produits = sum(
        payment["amount"]
        for payment in await va_service.client_payments(start_date, end_date)
    )
    charges = sum(
        payment["amount"]
        for payment in await va_service.supplier_payments(start_date, end_date)
    )
    resultat = produits - charges

    return {
        "charges": charges,
        "produits": produits,
        "resultat": resultat,
    }
