from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Mock des paiements clients et fournisseurs
mock_client_payments = [
    {"amount": 1500.00},
    {"amount": 2500.00},
]

mock_supplier_payments = [
    {"amount": 1000.00},
    {"amount": 500.00},
]


def test_compte_de_resultat():
    with (
        patch(
            "app.services.va_service.VAService.client_payments",
            new=AsyncMock(return_value=mock_client_payments),
        ),
        patch(
            "app.services.va_service.VAService.supplier_payments",
            new=AsyncMock(return_value=mock_supplier_payments),
        ),
    ):
        response = client.get("/compte_resultat/")

        assert response.status_code == 200

        expected_produits = sum(
            payment["amount"] for payment in mock_client_payments
        )  # 4000.00
        expected_charges = sum(
            payment["amount"] for payment in mock_supplier_payments
        )  # 1500.00
        expected_resultat = expected_produits - expected_charges  # 2500.00

        assert response.json() == {
            "charges": expected_charges,
            "produits": expected_produits,
            "resultat": expected_resultat,
        }
