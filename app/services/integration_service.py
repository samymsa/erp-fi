import os

import httpx
from dotenv import load_dotenv


class IntegrationService:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("KEPI_URL")
        if not self.base_url:
            raise ValueError("Missing KEPI_URL environment variable")

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
