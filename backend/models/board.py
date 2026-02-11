from __future__ import annotations

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, DateTime, String, ForeignKey
from datetime import datetime, timezone
from db import db
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import UserModel
    from .list import ListModel


class BoardModel(db.Model):
    __tablename__ = "boards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )

    user: Mapped[UserModel] = relationship(back_populates="boards")
    lists: Mapped[List[ListModel]] = relationship(
        back_populates="board", cascade="all, delete-orphan"
    )
