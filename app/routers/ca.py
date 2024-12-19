from datetime import date

from fastapi import APIRouter

from app.services import va

router = APIRouter(
    prefix="/ca",
)


@router.post("/")
async def ca(debut: date = date.min, fin: date = date.max):
    ventes = va.ventes(debut, fin)
    ca = sum(vente["total"] for vente in ventes)
    return {"ca": ca}
