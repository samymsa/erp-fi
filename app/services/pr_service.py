from app.services.integration_service import IntegrationService


class PRService:
    def __init__(self, integration_service: IntegrationService):
        self.integration_service = integration_service

    async def get_all_projects(self):
        return await self.integration_service.action("PR_PROJECTS_GET_ALL")

    async def get_project_by_id(self, project_id: str):
        return await self.integration_service.action(
            "PR_PROJECTS_GET_BY_ID", {"ID_projet": project_id}, {}
        )
