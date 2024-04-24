from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('process.env', '.env'),
        # env_file_encoding = 'utf-8'
    )
    debug: bool = True
    CYCLIC_DB: str = "CYCLIC_DB"
    CYCLIC_BUCKET_NAME: str = "CYCLIC_BUCKET_NAME"
    AWS_REGION: str = "AWS_REGION"
    AWS_ACCESS_KEY_ID: SecretStr = "AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY: SecretStr = "AWS_SECRET_ACCESS_KEY"
    AWS_SESSION_TOKEN: SecretStr = "AWS_SESSION_TOKEN"
    AWS_TABLE_ID: str = "AWS_TABLE_ID"


@lru_cache()
def get_settings():
    return Settings()
