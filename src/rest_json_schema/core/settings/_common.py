from functools import partial

from pydantic_settings import SettingsConfigDict

_model_config = partial(SettingsConfigDict, env_file=".env", extra="ignore")
