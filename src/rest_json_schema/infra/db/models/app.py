from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from domain.enums import StateEnum

from .base import Base


class AppModel(Base):
    __tablename__ = "app"

    kind: Mapped[str] = mapped_column(unique=True, kw_only=True)
    name: Mapped[str] = mapped_column(kw_only=True)
    version: Mapped[str] = mapped_column(kw_only=True)
    description: Mapped[str] = mapped_column(kw_only=True)
    state: Mapped[StateEnum] = mapped_column(kw_only=True)
    specification: Mapped[bytes] = mapped_column(type_=JSONB, kw_only=True)
    settings: Mapped[bytes] = mapped_column(type_=JSONB, kw_only=True)
