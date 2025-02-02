from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_pr_service
from app.services.pr_service import PRService

router = APIRouter(
    prefix="/rentabilite_projet",
)


class RentabiliteProjetResponse(BaseModel):
    rentabilite_projet: float


TJM = 324.12  # Tarif Journalier Moyen


@router.get(
    "",
    description="Calculer la rentabilité d'un projet",
    response_model=RentabiliteProjetResponse,
)
async def rentabilite_projet(
    project_id: str, pr_service: PRService = Depends(get_pr_service)
) -> dict:
    project = await pr_service.get_project_by_id(project_id)

    ca_projet = project["sale"]["amount"]
    charges_projet = project["workDaysNeeded"] * TJM

    rentabilite = ca_projet - charges_projet

    return {"rentabilite_projet": rentabilite}
