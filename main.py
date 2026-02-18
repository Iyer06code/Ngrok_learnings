from fastapi import FastAPI
from db import engine, Base
from routes.user import router as user_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(user_router, prefix="/user", tags=["User"])


@app.get("/")
async def root():
    return {"message": "Hello, World!"}