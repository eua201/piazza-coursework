#Adapted from class-4/solutions/auth-api/application.py
#https://github.com/warestack/cc/blob/4fc02cfbd95d5840b660ebb96eff91c208904472/class-4/solutions/auth-api/application.py
#Changes: titles, to personalise to Piazza.Changed model and database imports to the app package layout to avoid module not found error,
from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import auth



# Create the users table if it does not exist.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI for Piazza Assignment")

# All auth routes start with /auth.
app.include_router(auth.router, prefix="/auth")


@app.get("/")
def home():
    return {"message": "Piazza is running"}


@app.get("/health")
def health():
    return {"status": "ok"}

