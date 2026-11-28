#Adapted from class-4/solutions/auth-api/application.py
#https://github.com/warestack/cc/blob/4fc02cfbd95d5840b660ebb96eff91c208904472/class-4/solutions/auth-api/application.py
#Changes: titles, to personalise to Piazza.Changed model and database imports to the app package layout to avoid module not found error.
#References: 
from app import models  
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine
from app.models import seed_topics
from app.routers import auth,posts




# Create the users table if it does not exist.
@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    seed_topics()
    yield

app = FastAPI(title="FastAPI for Piazza Assignment",lifespan=lifespan)
app.include_router(auth.router, prefix="/auth",tags=["auth"])
app.include_router(posts.router, prefix="/auth", tags=["posts"])


@app.get("/")
def home():
    return {"message": "Piazza Platform"}

@app.get("/health")
def health():
    return {"status": "ok"}

