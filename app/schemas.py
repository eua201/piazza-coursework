##Adapted from Week 4 of Labs class-4/solutions/auth-api
#https://github.com/warestack/cc/blob/4fc02cfbd95d5840b660ebb96eff91c208904472/class-4/solutions/auth-api/schemas.py
#Changes: Username removed to match brief registration criteria

from pydantic import BaseModel, ConfigDict, EmailStr, Field

# Request body for registration.
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)


# Request body for login.
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Response body for a user.
# Notice that the password is not included.
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


# Response body returned after login.
class TokenResponse(BaseModel):
    access_token: str
    token_type: str