from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Données fictives pour les projets
mock_projects = [
    {"id": 1, "sale": {"amount": 10000.00}, "workDaysNeeded": 20},
    {"id": 2, "sale": {"amount": 15000.00}, "workDaysNeeded": 25},
    {"id": 3, "sale": {"amount": 20000.00}, "workDaysNeeded": 30},
]

TJM = 324.12  # Tarif Journalier Moyen


def test_rentabilite_projet():
    with patch(
        "app.services.pr_service.PRService.get_project_by_id",
        new=AsyncMock(return_value=mock_projects[0]),
    ):
        response = client.get("/rentabilite_projet/1")

        assert response.status_code == 200

        expected_ca = mock_projects[0]["sale"]["amount"]
        expected_charges = mock_projects[0]["workDaysNeeded"] * TJM
        expected_rentabilite = expected_ca - expected_charges

        assert response.json() == {
            "id": "1",
            "ca": round(expected_ca, 2),
            "charges": round(expected_charges, 2),
            "rentabilite": round(expected_rentabilite, 2),
        }


def test_rentabilite_projet_all():
    with patch(
        "app.services.pr_service.PRService.get_all_projects",
        new=AsyncMock(return_value=mock_projects),
    ):
        response = client.get("/rentabilite_projet/all")

        assert response.status_code == 200

        expected_results = [
            {
                "id": str(project["id"]),
                "ca": round(project["sale"]["amount"], 2),
                "charges": round(project["workDaysNeeded"] * TJM, 2),
                "rentabilite": round(
                    project["sale"]["amount"] - project["workDaysNeeded"] * TJM, 2
                ),
            }
            for project in mock_projects
        ]

        assert response.json() == expected_results
