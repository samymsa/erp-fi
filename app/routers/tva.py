from datetime import date

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_va_service
from app.services.va_service import VAService

router = APIRouter(
    prefix="/tva",
)


class TVAResponse(BaseModel):
    collectee: float
    deductible: float
    a_declarer: float


@router.get(
    "",
    description="Calculer la TVA à déclarer sur une période donnée",
    response_model=TVAResponse,
)
async def tva(
    start_date: date = date.min,
    end_date: date = date.max,
    va_service: VAService = Depends(get_va_service),
) -> dict:
    tax_rate = 0.2

    client_payments = await va_service.client_payments(start_date, end_date)
    supplier_payments = await va_service.supplier_payments(start_date, end_date)

    client_payments_amount = sum(payment["amount"] for payment in client_payments)
    supplier_payments_amount = sum(payment["amount"] for payment in supplier_payments)

    return {
        "collectee": client_payments_amount * tax_rate,
        "deductible": supplier_payments_amount * tax_rate,
        "a_declarer": client_payments_amount * tax_rate
        - supplier_payments_amount * tax_rate,
    }
