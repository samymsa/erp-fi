from fastapi import Depends

from app.services.integration_service import IntegrationService
from app.services.pr_service import PRService
from app.services.va_service import VAService


def get_integration_service():
    return IntegrationService()


def get_va_service(
    integration_service: IntegrationService = Depends(get_integration_service),
):
    return VAService(integration_service)


def get_pr_service(
    integration_service: IntegrationService = Depends(get_integration_service),
):
    return PRService(integration_service)
