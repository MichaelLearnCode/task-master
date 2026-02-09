from datetime import datetime, timezone
from db import db
from typing import List, TYPE_CHECKING
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, DateTime, Text
if TYPE_CHECKING:
    from .board import BoardModel

class UserModel(db.Model):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    username:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email:Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password:Mapped[str] = mapped_column(Text, nullable=False)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    boards:Mapped[List[BoardModel]] = relationship(back_populates='user',lazy='dynamic' ,cascade='all, delete-orphan')