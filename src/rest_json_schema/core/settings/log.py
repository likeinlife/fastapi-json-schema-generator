from pydantic import Field
from pydantic_settings import BaseSettings

from ._common import _model_config


class LoggingSettings(BaseSettings):
    model_config = _model_config(env_prefix="LOGGING_")

    level: str = Field(default="INFO", init=False)
    json_format: bool = Field(default=False, init=False)
