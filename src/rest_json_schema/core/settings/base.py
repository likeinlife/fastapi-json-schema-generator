from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

from ._common import _model_config
from .db import DBSettings
from .log import LoggingSettings


class AppSettings(BaseSettings):
    model_config = _model_config(env_prefix="APP_")

    name: str = Field(init=False)
    version: str = Field(init=False)
    debug: bool = Field(default=False, init=False)


class Settings(BaseModel):
    app: AppSettings = Field(default_factory=AppSettings)
    log: LoggingSettings = Field(default_factory=LoggingSettings)
    db: DBSettings = Field(default_factory=DBSettings)
