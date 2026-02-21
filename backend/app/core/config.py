from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "OmniCore API"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    access_token_minutes: int = 60


settings = Settings()
