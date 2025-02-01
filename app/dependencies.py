from app.services.integration_service import IntegrationService
from app.services.va_service import VAService


def get_integration_service():
    return IntegrationService()


def get_va_service():
    return VAService()
