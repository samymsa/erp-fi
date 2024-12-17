import os

import requests
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    os.getenv("KEPI_URL") + "/register",
    json={"appKey": "FI", "url": os.getenv("APP_URL")},
)

print(f"Status code: {response.status_code}")
print(f"Response: {response.text}")
