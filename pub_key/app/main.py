from fastapi import FastAPI
import os

app = FastAPI()

os.chdir('../')

# to run in docker file keep the file path as code
# to run locally delete the code prefix and generate the public key and private key under pub_key directory
public_key = open('code/public_key.pem', 'r').read()


@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/publicKey")
async def root():
    return public_key