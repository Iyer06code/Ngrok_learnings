from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import User
from repositories.user_repo import UserRepo
from schemas.user_schemas import UserSchema

router = APIRouter()

# ---------------------------------------------------
# Create User
# ---------------------------------------------------

@router.post("/users")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)

    existing_user = user_repo.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    db_user = User(email=user.email, password=user.password)
    user_repo.add_user(db_user)

    return {"message": "User created successfully"}

# ---------------------------------------------------
# Get All Users
# ---------------------------------------------------

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    users = user_repo.get_all_users()
    return users

# ---------------------------------------------------
# Get User By ID
# ---------------------------------------------------

@router.get("/users/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    user = user_repo.get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
