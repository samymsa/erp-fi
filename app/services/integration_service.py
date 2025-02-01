import httpx

from app.config import settings


class IntegrationService:
    def __init__(self):
        self.base_url = settings.kepi_url
        self.client = httpx.AsyncClient()

    async def action(
        self, key: str, params: dict | None = None, body: dict | None = None
    ):
        payload = {
            "key": key,
            "params": params,
            "body": body,
        }
        response = await self.client.post(f"{self.base_url}/action", json=payload)
        response.raise_for_status()
        return response.json()
