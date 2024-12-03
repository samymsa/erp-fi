from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calcul_ca():
    response = client.post(
        "/ca/",
        json=[
            {"prix_unitaire": "100.50", "quantite": 10},
            {"prix_unitaire": "50.25", "quantite": 5},
        ],
    )
    assert response.status_code == 200
    expected_total = 1005.00 + 251.25
    assert response.json() == {"chiffres_affaires_total": expected_total}
