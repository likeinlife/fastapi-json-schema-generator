from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings

from ._common import _model_config


class DBSettings(BaseSettings):
    model_config = _model_config(env_prefix="DB_")

    password: SecretStr = Field(init=False)
    user: SecretStr = Field(init=False)
    host: str = Field(init=False)
    port: int = Field(default=5432, init=False)
    db_name: str = Field(default="dialog", init=False)

    def get_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.user.get_secret_value()}:"
            f"{self.password.get_secret_value()}@{self.host}:{self.port}/{self.db_name}"
        )
