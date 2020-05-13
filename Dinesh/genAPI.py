from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

import uuid

import Generator

app = FastAPI()

app.mount("/designs",StaticFiles(directory="designs"),name="designs")

@app.get("/generate")
async def generate():
    unique_name = uuid.uuid1().hex
    Generator.generate_image("designs/{}.png".format(unique_name))
    response = RedirectResponse(url="/designs/{}.png".format(unique_name))
    return response

