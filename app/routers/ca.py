from datetime import date

from fastapi import APIRouter

router = APIRouter(
    prefix="/ca",
)


@router.post("/")
async def ca(debut: date, fin: date):
    # récupérer toutes les ventes entre les dates debut et fin
    return {"ca": 0}
