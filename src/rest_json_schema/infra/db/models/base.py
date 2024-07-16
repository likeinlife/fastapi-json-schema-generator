import datetime as dt
import uuid

import sqlalchemy as sa
from sqlalchemy import orm


class Base(orm.MappedAsDataclass, orm.DeclarativeBase):
    created_at: orm.Mapped[dt.datetime] = orm.mapped_column(server_default=sa.func.now())
    id: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        default_factory=uuid.uuid4,
    )
