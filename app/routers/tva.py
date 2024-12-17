from datetime import date

from fastapi import APIRouter

router = APIRouter(
    prefix="/tva",
)


@router.post("/")
async def tva(debut: date, fin: date):
    # récupérer toutes les ventes entre les dates debut et fin --> tva collectée
    # récupérer toutes les achats entre les dates debut et fin --> tva déductible
    # calculer la tva à payer
    tva_collectee = 0
    tva_deductible = 0
    return {"tva": tva_collectee - tva_deductible}
