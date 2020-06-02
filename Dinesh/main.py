from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

import uuid

import Generator

app = FastAPI()

app.mount("/dinesh/designs",StaticFiles(directory="designs"),name="designs")

@app.get("/dinesh/generate")
async def generate(redirect: bool = True):
    unique_name = uuid.uuid1().hex
    Generator.generate_image("designs/{}.jpg".format(unique_name))
    if redirect:
        response = RedirectResponse(url="designs/{}.jpg".format(unique_name))
        return response

    return {
            "path":"dinesh/designs/{}.jpg".format(unique_name)
            }
