from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import create_token

router = APIRouter()

class AuthRequest(BaseModel):
    username: str
    password: str

@router.post('/login')
def login(auth: AuthRequest):
    # For demonstration purposes, we will use hardcoded credentials.
    # In a real application, you should verify the username and password against a database.
    if auth.username == "admin" and auth.password == "admin":
        token = create_token({'sub': auth.username})
        return {'access_token': token}
    return {'error': "Invalid Credentials"}