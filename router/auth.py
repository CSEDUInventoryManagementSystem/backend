import models
import schemas
import utils
import oauth2
import database
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session




import uuid
from datetime import datetime, timedelta




router = APIRouter(
    tags=["Authentication"]
)

@router.post("/signup", response_model=schemas.SignUpOut, status_code=201)
def signup(request: schemas.SignUp, db: Session = Depends(database.get_db)):
    if db.query(models.User).filter(models.User.email == request.email).first():
        raise HTTPException(status_code=400, detail="EMAILERROR")
    
    user = models.User(
        email=request.email,
        hashedPassword=utils.hash(request.password),
        firstName=request.firstName,
        lastName=request.lastName,
        role=request.role,
        phone=request.phone,
        userName=utils.createUserName(request.firstName + request.lastName),
        status="PENDING"

    )

    db.add(user)
    db.commit()
    db.refresh(user)

    utils.sendEmail(
        "Welcome to CSEDU Inventory Management System",
        "Your account has been created successfully. Please wait for the admin to verify your account",
        user.email
    )

    userOut = schemas.SignUpOut(
        email=user.email,
        firstName=user.firstName,
        lastName=user.lastName,
        role=user.role,
        phone=user.phone,
        userName=user.userName,
        status=user.status
    )

    return userOut