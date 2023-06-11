from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from internal.auth import Token, login

app = APIRouter()


@app.post("/api/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return login(form_data.username, form_data.password)
