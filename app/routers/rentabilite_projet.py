from fastapi import APIRouter

router = APIRouter(
    prefix="/rentabilite_projet",
)


@router.post("/")
async def rentabilite_projet(id_projet: int):
    # calculer le ca du projet
    # calculer les charges du projet
    # calculer la rentabilité du projet
    ca_projet = 0
    charges_projet = 0
    return {"rentabilite_projet": ca_projet - charges_projet}
