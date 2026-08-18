from fastapi import Request, HTTPException, status, Depends
from src.utils.settings import settings
from sqlalchemy.orm import Session

from src.users.model import UserModel
from src.utils.db import get_db
import jwt
from datetime import datetime

def is_authenticated(request:Request, db:Session=Depends(get_db)):
    token = request.headers.get("authorization")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization token is missing")
    print("Token:", token)
    token = token.split(" ")[-1]
    data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    print("Payload:", data)

    user_id = data.get("id")
    exp_time = int(data.get("exp"))
    current_time = datetime.now().timestamp()
    if current_time > exp_time:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "your token has been expired")
    
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "you are anauthorized")
    return user