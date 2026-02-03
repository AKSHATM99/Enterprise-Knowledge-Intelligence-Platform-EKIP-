from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "EKIP"
    debug: bool = True

    groq_api_key: str | None = None

    class Config:
        env_file = ".env"
        extra = "forbid"   

settings = Settings()
