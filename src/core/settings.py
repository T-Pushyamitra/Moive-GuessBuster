from src.core.base import AppEnvironment, AppSettings
from functools import lru_cache
from os import environ

class AppStagingSettings(AppSettings):
    ENVIRONMENT: AppEnvironment = AppEnvironment.STAGING
    DESCRIPTION: str = f"Application ({ENVIRONMENT})."
    IS_DEBUG: bool = True


class AppDevelopmentSettings(AppSettings):
    ENVIRONMENT: AppEnvironment = AppEnvironment.DEVELOPMENT
    DESCRIPTION: str = f"Application ({ENVIRONMENT})."
    IS_DEBUG: bool = True


class AppProductionSettings(AppSettings):
    ENVIRONMENT: AppEnvironment = AppEnvironment.PRODUCTION
    DESCRIPTION: str = f"Application ({ENVIRONMENT})."


class FactoryAppSettings:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> AppSettings:
        if self.environment == AppEnvironment.PRODUCTION:
            return AppProductionSettings()
        elif self.environment == AppEnvironment.STAGING:
            return AppStagingSettings()
        return AppDevelopmentSettings()


@lru_cache()
def get_settings() -> AppSettings:
    return FactoryAppSettings(environment=environ["APP_ENV"])()


settings = get_settings()