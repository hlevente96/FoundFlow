from .database import SessionLocal
from passlib.context import CryptContext
from .models import Users
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from starlette.responses import RedirectResponse
import os
from dotenv import load_dotenv

load_dotenv("/Users/leventeharsanyi/Desktop/Herman_Support/secret.env")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/auth/token')

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()

def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user or not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, role: str, first_name:str, expires_delta: timedelta):
    encode = {'sub': username, 'id':user_id, 'role': role, 'fname': first_name}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        first_name: str = payload.get('fname')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user')
        return {'username': username, 'id':user_id, 'user_role': user_role, 'first_name': first_name}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user')

def redirect_to_login():
    redirect_response = RedirectResponse(url="/auth/login-page",
                                         status_code = status.HTTP_302_FOUND)
    redirect_response.delete_cookie(key="access_token")
    return redirect_response