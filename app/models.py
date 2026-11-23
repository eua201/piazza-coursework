#Adapted from Week 4 of Labs class-4/solutions/auth-api
#https://github.com/warestack/cc/blob/4fc02cfbd95d5840b660ebb96eff91c208904472/class-4/solutions/auth-api/models.py
#Changes: Database imports from Base in my module, i've added classes, extended the number of classes to include, posts and comments etc.
#Reference :1. https://docs.python.org/3/library/datetime.html#aware-and-naive-objects 2.https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.DateTime (Accessed 22nd of November 2026) used to understand how datetime works.

from datetime import datetime, timezone
from sqlalchemy import Column, ForeignKey, Integer, String, Text, UniqueConstraint,DateTime

from app.database import Base

def utc_now():
    return datetime.now(timezone.utc).replace(tzinfo=None)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=utc_now)
    expires_at = Column(DateTime, nullable=False)

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


class PostTopic(Base):
    __tablename__ = "post_topic"

    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False, primary_key=True)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable=False, primary_key= True)

    __table_args__ = (
        UniqueConstraint("post_id", "topic_id", name="uq_post_topic"),
    )


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=utc_now)

class Reaction(Base):
    __tablename__ = "reactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    reaction_type = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=utc_now)
    __table_args__ = (
        UniqueConstraint("post_id", "user_id", name="uq_reaction"),
    )