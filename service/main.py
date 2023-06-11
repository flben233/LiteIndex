import json
import os

import uvicorn
from fastapi import FastAPI, Request, Response

from internal.auth import auth
from routers import tabs, login, images, paste, performance

app = FastAPI()
app.include_router(tabs.app)
app.include_router(login.app)
app.include_router(images.app)
app.include_router(paste.app)
app.include_router(performance.app)


@app.middleware("http")
async def login_interceptor(request: Request, call_next):
    # check if the request is a login request
    exclusive_path = {"/api/login", "/docs", "/openapi.json", "/api/images"}
    for p in exclusive_path:
        if request.url.path.find(p) == 0:
            return await call_next(request)
    # check if the request is authorized
    if "authorization" in request.headers.keys():
        token = request.headers["authorization"]
        if auth(token):
            return await call_next(request)
    return Response(status_code=401, content="Unauthorized", headers={"WWW-Authenticate": "Bearer"})


if __name__ == "__main__":
    if not os.path.exists("items.json"):
        with open("items.json", "w") as f:
            json.dump([], f)
        print("items.json created")
    with open("items.json", "r") as f:
        tabs.items = json.load(f)
    uvicorn.run(app, host="0.0.0.0", port=8000, access_log=False)
