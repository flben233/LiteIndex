import os.path
import uuid

from fastapi import UploadFile, APIRouter, Response
from fastapi.responses import StreamingResponse
from config import IMAGE_PATH, WEB_ROOT

app = APIRouter()


@app.post("/api/icons/")
async def upload_icon(image: UploadFile):
    if not os.path.exists("./images"):
        os.mkdir("./images")
    uid = uuid.uuid4()
    with open(f"{IMAGE_PATH}/{uid}.png", "wb") as i:
        i.write(image.file.read())
    return {"url": f"/api/images/{uid}.png"}


@app.get("/api/images/{uid}.png")
async def download_image(uid: str):
    try:
        i = open(f"{IMAGE_PATH}/{uid}.png", "rb")
    except FileNotFoundError:
        return Response(status_code=404)
    return StreamingResponse(i)


@app.post("/api/images/wallpaper/")
def upload_image(image: UploadFile):
    tmp = image.file.read()
    with open(f"{WEB_ROOT}/wallpaper.png", "wb") as j:
        j.write(tmp)
    return {"status": "success"}
