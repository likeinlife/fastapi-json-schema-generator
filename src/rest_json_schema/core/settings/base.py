from pydantic import Field
from pydantic_settings import BaseSettings

from ._common import _model_config
from .db import DBSettings
from .log import LoggingSettings


class AppSettings(BaseSettings):
    model_config = _model_config(env_prefix="APP_")

    name: str = Field(init=False)
    version: str = Field(init=False)
    debug: bool = Field(default=False, init=False)


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    log: LoggingSettings = LoggingSettings()
    db: DBSettings = DBSettings()
