from src.users.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.users.model import UserModel
from src.utils.settings import settings
from fastapi import HTTPException, status, Request, BackgroundTasks
from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta
from src.utils.mail import send_registration_email


password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


async def register(body: UserSchema, db: Session, bg_tasks: BackgroundTasks):
    is_user = db.query(UserModel).filter(UserModel.username==body.username).first()
    if is_user:
        raise HTTPException(400, detail="username already exists...")
    
    is_user = db.query(UserModel).filter(UserModel.email==body.email).first()
    if is_user:
        raise HTTPException(400, detail="email is already exists...")
    

    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name = body.name,
        username=body.username,
        hash_password= hash_password,
        email= body.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    ## send email to user after registration
    
    bg_tasks.add_task(send_registration_email, [new_user.email])

def Login_user(body:LoginSchema, db:Session):
    user = db.query(UserModel).filter(UserModel.username==body.username).first()

    if not user :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You entered wrong username")
    
    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You entered wrong password")

    exp_time = datetime.now()+timedelta(minutes=settings.EXP_TIME)
    token = jwt.encode({"id": user.id, "exp": exp_time}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return{"token": token}

def is_authenticated(request:Request, db:Session):
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
