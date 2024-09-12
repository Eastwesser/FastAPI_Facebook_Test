from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    page_access_token: str
    api_version: str
    debug: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
