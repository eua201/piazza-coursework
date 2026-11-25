
##Adapted from Week 4 of Labs class-4/solutions/auth-api
#https://github.com/warestack/cc/blob/4fc02cfbd95d5840b660ebb96eff91c208904472/class-4/solutions/auth-api/routers/auth.py
#Changes: Changed model and database imports to the app package layout to avoid module not found error, username removed and password column renamed to password_hash to match my diagram.

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import app.models
import app.schemas
from app.database import get_db
from app.security import create_access_token, hash_password, verify_password

router = APIRouter()


@router.post("/register", response_model=app.schemas.UserResponse, status_code=201)
def register(user: app.schemas.UserCreate, db: Session = Depends(get_db)):
    # Check whether another user already has this email.
    existing_user = db.query(app.models.User).filter(app.models.User.email == user.email).first()

    if existing_user is not None:
        raise HTTPException(status_code=409, detail="Email already registered")

    # Create a database user.
    # The password is hashed before it is stored.
    db_user = app.models.User(
        email=user.email,
        password_hash=hash_password(user.password)
    )

    # Save the new user and reload it so the generated ID is available.
    db.add(db_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email already registered")
    db.refresh(db_user)
    return db_user


@router.post("/login", response_model=app.schemas.TokenResponse)
def login(user_login: app.schemas.UserLogin, db: Session = Depends(get_db)):
    # Find the user by email.
    user = db.query(app.models.User).filter(app.models.User.email == user_login.email).first()

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Compare the submitted password with the stored hash.
    if not verify_password(user_login.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Put the user's email in the token subject.
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"} 