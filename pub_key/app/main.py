from fastapi import FastAPI
import os

app = FastAPI()

os.chdir('..')
public_key = open('public_key.pem', 'r').read()

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/publicKey")
async def root():
    return public_key