from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer, DateTime, Text, Boolean, ForeignKey
from datetime import datetime, timezone
from db import db
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .task import TaskModel

class SubtaskModel(db.Model):
    __tablename__ = "subtasks"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    content:Mapped[str] = mapped_column(Text, nullable=False)
    is_completed:Mapped[bool] = mapped_column(Boolean, default=False)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    task_id:Mapped[int] = mapped_column(Integer, ForeignKey('tasks.id'), nullable=False)

    task:Mapped['TaskModel'] = relationship(back_populates='subtasks')