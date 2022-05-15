from fastapi import FastAPI
from random_string import random_string

app = FastAPI()


@app.get("/otp/get")
async def get_otp():
    return random_string()


@app.post("/otp/send")
async def send_mail():
    return random_string()
