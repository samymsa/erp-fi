from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/rentabilite_projet",
)


class RentabiliteProjetResponse(BaseModel):
    rentabilite_projet: float


@router.get(
    "",
    description="Calculer la rentabilité d'un projet",
    response_model=RentabiliteProjetResponse,
)
async def rentabilite_projet(id_projet: int):
    # calculer le ca du projet
    # calculer les charges du projet
    # calculer la rentabilité du projet
    ca_projet = 0
    charges_projet = 0
    return {"rentabilite_projet": ca_projet - charges_projet}
