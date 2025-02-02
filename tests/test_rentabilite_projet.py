from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Données fictives pour le projet
mock_project = {"sale": {"amount": 10000.00}, "workDaysNeeded": 20}

TJM = 324.12  # Tarif Journalier Moyen


def test_rentabilite_projet():
    with patch(
        "app.services.pr_service.PRService.get_project_by_id",
        new=AsyncMock(return_value=mock_project),
    ):
        response = client.get("/rentabilite_projet/", params={"project_id": "123"})

        assert response.status_code == 200

        expected_ca = mock_project["sale"]["amount"]  # 10000.00
        expected_charges = mock_project["workDaysNeeded"] * TJM  # 20 * 324.12 = 6482.4
        expected_rentabilite = expected_ca - expected_charges  # 10000 - 6482.4 = 3517.6

        assert response.json() == {"rentabilite_projet": expected_rentabilite}
