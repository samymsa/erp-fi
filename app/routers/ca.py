from datetime import date

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_va_service
from app.services.va_service import VAService

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
async def ca(
    start_date: date = date.min,
    end_date: date = date.max,
    va_service: VAService = Depends(get_va_service),
) -> dict:
    client_payments = await va_service.client_payments(start_date, end_date)
    return {"ca": sum(payment["amount"] for payment in client_payments)}
