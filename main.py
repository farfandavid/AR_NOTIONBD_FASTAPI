from typing import Union
from fastapi import FastAPI
import requests
import json
from config import settings
# Creacion de una aplicacion FastApi

app = FastAPI()


@app.get("/")
def read_root():
    url = settings.BD_URL
    payload = ""
    headers = {
        'Authorization': settings.SECRETKEY,
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)
    return response.json()["results"]
