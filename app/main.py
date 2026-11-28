#Adapted from class-4/solutions/auth-api/application.py
#https://github.com/warestack/cc/blob/4fc02cfbd95d5840b660ebb96eff91c208904472/class-4/solutions/auth-api/application.py
#Changes: titles, to personalise to Piazza.Changed model and database imports to the app package layout to avoid module not found error.
#References: Schafer, C. (2026) Python FastAPI Tutorial (Part 7): Sync vs Async - Converting Your App to Asynchronous. [Online video].Available at: https://www.youtube.com/watch?v=2JPDt-Jp6fM (Accessed: 28 November 2026).is why I used FastAPI's lifespan
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import engine
from app import models
from app.models import seed_topics
from app.routers import auth



#creates all tables and seeds four topics
@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    seed_topics()
    yield

app = FastAPI(title="FastAPI for Piazza Assignment",lifespan=lifespan)
app.include_router(auth.router, prefix="/auth",tags=["auth"])


@app.get("/")
def home():
    return {"message": "Piazza Platform"}

@app.get("/health")
def health():
    return {"status": "ok"}

