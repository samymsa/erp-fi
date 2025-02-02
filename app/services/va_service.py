from datetime import date

import httpx

from app.services.integration_service import IntegrationService


class VAService:
    def __init__(self, integration_service: IntegrationService):
        self.integration_service = integration_service
        self.client = httpx.AsyncClient()

    async def client_payments(
        self, start_date: date = date.min, end_date: date = date.max
    ):
        data = await self.integration_service.action("VA_LIST_CLIENT_PAYMENT")
        filtered_data = [
            payment
            for payment in data
            if start_date.strftime("%Y-%m-%d")
            <= payment["paymentDate"]
            <= end_date.strftime("%Y-%m-%d")
        ]

        return filtered_data

    async def supplier_payments(
        self, start_date: date = date.min, end_date: date = date.max
    ):
        data = await self.integration_service.action("VA_LIST_SUPPLIER_PAYMENT")
        filtered_data = [
            payment
            for payment in data
            if start_date.strftime("%Y-%m-%d")
            <= payment["paymentDate"]
            <= end_date.strftime("%Y-%m-%d")
        ]

        return filtered_data
