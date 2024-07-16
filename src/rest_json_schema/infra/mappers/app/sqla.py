from domain.entities import App
from infra.db.models import AppModel
from infra.mappers.interfaces import ISQLAlchemyMapper


class SQLAAppMapper(ISQLAlchemyMapper[App, AppModel]):
    def from_orm(self, orm: AppModel) -> App:
        return App(
            id=orm.id,
            kind=orm.kind,
            name=orm.name,
            version=orm.version,
            description=orm.description,
            specification=orm.specification,
            settings=orm.settings,
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
            specification=(dto.specification),
            settings=(dto.settings),
            state=dto.state,
            created_at=dto.created_at,
        )
