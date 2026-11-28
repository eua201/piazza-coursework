##Adapted from Week 4 of Labs class-4/solutions/auth-api
#https://github.com/warestack/cc/blob/4fc02cfbd95d5840b660ebb96eff91c208904472/class-4/solutions/auth-api/schemas.py
#Changes: Username removed to match brief registration criteria, added post, comment, topic
#References: Schafer, C. (2026) Python FastAPI Tutorial (Part 4): Pydantic Schemas - Request and Response Validation. [Online video]. Available at: https://www.youtube.com/watch?v=9GHxnttXxrA (Accessed: 28 November 2026).inspired schema structure, extrapolated comment class from his use of posts.
#References: Schafer, C. (2026) Python FastAPI Tutorial (Part 5): Adding a Database - SQLAlchemy Models and Relationships. [Online video].Available at: https://www.youtube.com/watch?v=NvOV3ig2tGY (Accessed: 28 November 2026).helped me understand wiring together main, routers, schemas and the config dict function.
#References: https://vizlearn.in/pydantic/computed_fields.html (Accessed 28 Nov 2026) used for expired at date time calculation. 

#HOW DATA ENTERS AND LEAVES THE API 
from typing import Annotated
from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints, computed_field, field_validator
from datetime import datetime,timezone
from app.models import ReactionType, TopicName
from app import models 
NonBlankStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    
# --------------------Users--------------------
class UserCreate(BaseModel):
    email: EmailStr = Field(max_length=120)
    password: str = Field(min_length=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str

# --------------------Comments--------------------
class CommentBase(BaseModel):
    body: str = Field(min_length=1)


class CommentCreate(CommentBase):
    body: NonBlankStr


class CommentResponse(BaseModel):
      body: str
      post_id: int
      user_id:int
      id:int
      created_at: datetime
      model_config = ConfigDict(from_attributes=True)

# --------------------Posts--------------------
class PostBase(BaseModel):
    title: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]
    body: NonBlankStr
    expires_at: datetime
    topics:list[TopicName] = Field(min_length=1, max_length=4)

    @field_validator("topics")
    @classmethod
    def unique_topics(cls, v: list[TopicName]) -> list[TopicName]:
        if len(set(v)) != len(v):
            raise ValueError("Topics must be unique")
        return v

    @field_validator("expires_at")
    @classmethod
    def expires_at_must_be_aware(cls, v: datetime) -> datetime:
        if v.tzinfo is None:
            raise ValueError("expires_at must include a timezone, e.g. 2026-12-01T12:00:00Z")
        return v

class PostCreate(PostBase):
    pass


class PostResponse(BaseModel):
    id: int
    title: str
    body: NonBlankStr
    created_at: datetime
    expires_at: datetime
    user_id:int
    topics: list[TopicName]
    likes:int
    dislikes:int
    comments:list[CommentResponse]
    model_config = ConfigDict(from_attributes=True)

    @field_validator("topics", mode="before")
    @classmethod
    def rows_to_names(cls, v):
         return [t.name if hasattr(t,"name")else t for t in v]

    @computed_field
    @property
    def status(self)->str:
        exp = self.expires_at
        if exp.tzinfo is not None:
            exp = exp.astimezone(timezone.utc).replace(tzinfo=None)
        now = models.utc_now()
        return "Live" if exp > now else "Expired"

    
# --------------------Reactions--------------------
class ReactionBase(BaseModel):
    value: ReactionType

class ReactionCreate(ReactionBase):
    pass

class ReactionCounts(BaseModel):
     likes: int
     dislikes: int



