from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_pr_service
from app.services.pr_service import PRService

router = APIRouter(
    prefix="/rentabilite_projet",
)


TJM = 324.12  # Tarif Journalier Moyen, arbitraire


def _rentabilite_projet(project: dict) -> dict:
    ca = project["sale"]["amount"]
    charges = project["workDaysNeeded"] * TJM
    rentabilite = ca - charges

    return {
        "id": str(project["id"]),
        "ca": round(ca, 2),
        "charges": round(charges, 2),
        "rentabilite": round(rentabilite, 2),
    }


class RentabiliteProjetResponse(BaseModel):
    id: str
    ca: float
    charges: float
    rentabilite: float


@router.get(
    "/all",
    description="Calculer la rentabilité de tous les projets",
    response_model=list[RentabiliteProjetResponse],
)
async def rentabilite_projet_all(
    pr_service: PRService = Depends(get_pr_service),
) -> list[dict]:
    projects = await pr_service.get_all_projects()
    return [_rentabilite_projet(project) for project in projects]


@router.get(
    "/{project_id}",
    description="Calculer la rentabilité d'un projet",
    response_model=RentabiliteProjetResponse,
)
async def rentabilite_projet(
    project_id: str, pr_service: PRService = Depends(get_pr_service)
) -> dict:
    project = await pr_service.get_project_by_id(project_id)
    return _rentabilite_projet(project)
