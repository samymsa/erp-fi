from datetime import date

import httpx


class VAService:
    base_url = "https://livl-erp-api.goudale.tgimenez.fr/api/"

    def __init__(self):
        self.client = httpx.AsyncClient()

    async def client_payments(
        self, start_date: date = date.min, end_date: date = date.max
    ):
        response = await self.client.get(self.base_url + "client-payments")
        data = response.json()
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
        response = await self.client.get(self.base_url + "supplier-payments")
        data = response.json()
        filtered_data = [
            payment
            for payment in data
            if start_date.strftime("%Y-%m-%d")
            <= payment["paymentDate"]
            <= end_date.strftime("%Y-%m-%d")
        ]

        return filtered_data
