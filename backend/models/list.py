from __future__ import annotations

from sqlalchemy.orm import mapped_column, Mapped, relationship
from db import db
from datetime import datetime, timezone
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Integer, ForeignKey, Float, DateTime

if TYPE_CHECKING:
    from .board import BoardModel
    from .task import TaskModel


class ListModel(db.Model):
    __tablename__ = "lists"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    order_index: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    board_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("boards.id"), nullable=False
    )

    board: Mapped[BoardModel] = relationship(back_populates="lists")
    tasks: Mapped[List[TaskModel]] = relationship(
        back_populates="list", cascade="all, delete-orphan"
    )
