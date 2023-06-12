from fastapi import APIRouter, Form

content = ""

app = APIRouter()


@app.get("/api/paste")
async def get_paste():
    return content


@app.post("/api/paste")
async def set_paste(text: str = Form()):
    global content
    content = text
    return {"status": "success"}


@app.delete("/api/paste")
async def delete_paste():
    global content
    content = ""
    return {"status": "success"}
