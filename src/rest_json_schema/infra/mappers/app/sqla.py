import orjson

from domain.entities import App
from infra.db.models import AppModel
from infra.mappers.interfaces import ISQLAlchemyMapper


class SQLAAppMapper(ISQLAlchemyMapper[App, AppModel]):
    def from_orm(self, orm: AppModel) -> App:
        specification = orjson.loads(orm.specification)
        settings = orjson.loads(orm.settings)
        return App(
            id=orm.id,
            kind=orm.kind,
            name=orm.name,
            version=orm.version,
            description=orm.description,
            specification=specification,
            settings=settings,
            state=orm.state,
            created_at=orm.created_at,
        )

    def to_orm(self, dto: App) -> AppModel:
        return AppModel(
            id=dto.id,
            kind=dto.kind,
            name=dto.name,
            version=dto.version,
            description=dto.description,
            specification=orjson.dumps(dto.specification),
            settings=orjson.dumps(dto.settings),
            state=dto.state,
            created_at=dto.created_at,
        )
