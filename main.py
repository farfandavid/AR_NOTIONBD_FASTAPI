from typing import Union
from fastapi import FastAPI
import requests
import json
from config import settings
from fastapi.middleware.cors import CORSMiddleware
# Creacion de una aplicacion FastApi

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://arirockart.com.ar/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
