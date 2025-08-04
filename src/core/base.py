
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from logging import INFO
from pathlib import Path
from enum import Enum

from os import environ

env_path = Path(__file__).resolve().parents[2] / ".env"

load_dotenv(dotenv_path=env_path)

class AppEnvironment(str, Enum):
    STAGING = "staging"
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    
class AppSettings(BaseSettings):
    TITLE: str = "Movie GuessBuster"
    VERSION: str = environ.get("APP_VERSION")
    TIMEZONE: str = "UTC"
    DESCRIPTION: str = ""
    IS_DEBUG: bool = False
    API_PREFIX: str = environ.get("API_PREFIX")
    DOCS_URL: str = environ.get("DOCS_URL")
    REDOC_URL: str = environ.get("REDOC_URL")

    HOST: str = environ.get("SERVER_HOST")
    PORT: int = int(environ.get("SERVER_PORT"))
    WORKERS: int = int(environ.get("SERVER_WORKERS"))
    IS_ALLOWED_CREDENTIALS: bool = bool(environ.get("IS_ALLOWED_CREDENTIALS"))
    ALLOWED_ORIGIN_LIST: list[str] = ["*"]
    ALLOWED_METHOD_LIST: list[str] = [
        environ.get("METHOD_1"),
        environ.get("METHOD_2"),
        environ.get("METHOD_3"),
        environ.get("METHOD_4"),
        environ.get("METHOD_5"),
    ]
    ALLOWED_HEADER_LIST: list[str] = [environ.get("ALL_HEADERS")]

    LOGGING_LEVEL: int = INFO
    LOGGERS: tuple[str, str] = (environ.get("ASGI_LOGGER"), environ.get("ACCESS_LOGGER"))

    model_config = SettingsConfigDict(
        env_file=f"{Path().resolve()}/.env",
        case_sensitive=True,
        validate_assignment=True,
        extra="allow",
    )

    @property
    def set_app_attributes(self) -> dict[str, str]:
        """
        Set all `FastAPI` class' attributes with the custom values defined in `BackendBaseSettings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.IS_DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "redoc_url": self.REDOC_URL,
            "api_prefix": self.API_PREFIX,
        }
    