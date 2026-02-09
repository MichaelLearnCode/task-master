from sqlalchemy.orm import mapped_column,Mapped, relationship
from db import db
from datetime import datetime, timezone
from sqlalchemy import Integer, String, DateTime, Text, Float, ForeignKey
from typing import TYPE_CHECKING, List, Optional
if TYPE_CHECKING:
    from .list import ListModel
    from .subtask import SubtaskModel

class TaskModel(db.Model):
    __tablename__ = "tasks"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)

    title:Mapped[str] = mapped_column(String(255), nullable=False)
    description:Mapped[str] = mapped_column(Text)
    order_index:Mapped[float] = mapped_column(Float, nullable=False)
    priority:Mapped[str] = mapped_column(String(20), default = 'medium')
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    due_date:Mapped[Optional[datetime]] = mapped_column(DateTime)
    list_id:Mapped[int] = mapped_column(Integer, ForeignKey('lists.id'), nullable=False)


    list:Mapped[ListModel] = relationship(back_populates='tasks')
    subtasks:Mapped[List[SubtaskModel]] = relationship(back_populates='task', cascade='all, delete-orphan', lazy='dynamic')