from fastapi import Depends

from app.dependencies import get_integration_service
from app.services.integration_service import IntegrationService


class PRService:
    base_url = "http://82.67.2.10:5000"

    def __init__(self):
        self.integration_service: IntegrationService = Depends(get_integration_service)

    def get_all_projects(self):
        response = self.integration_service.action("PR_PROJECTS_GET_ALL")
        data = response.json()
        return data

    def get_project_by_id(self, project_id: str):
        response = self.integration_service.action("PR_PROJECTS_GET_BY_ID", {"ID_projet": project_id}, {})
        data = response.json()
        return data