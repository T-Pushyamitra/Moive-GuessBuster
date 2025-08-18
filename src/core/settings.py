from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, class_mapper, ColumnProperty, RelationshipProperty

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

__DATABASE_URL = "postgresql+psycopg://user:pass@localhost:52003/db"  # Replace with your actual DB

__engine = create_engine(
    __DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=__engine)

class Base(DeclarativeBase):
    __abstract__ = True 
    
    def to_dict(self, include_relationships=True, visited=None):
            if visited is None:
                visited = set()
    
            cls = self.__class__
            if (cls, self.id) in visited:
                return f"<{cls.__name__} already visited>"
    
            visited.add((cls, self.id))
    
            result = {}
            mapper = class_mapper(cls)
    
            # Columns (regular fields)
            for attr in mapper.iterate_properties:
                if isinstance(attr, ColumnProperty):
                    result[attr.key] = getattr(self, attr.key)
    
                elif include_relationships and isinstance(attr, RelationshipProperty):
                    value = getattr(self, attr.key)
                    if value is None:
                        result[attr.key] = None
                    elif attr.uselist:
                        result[attr.key] = [item.to_dict(include_relationships=False, visited=visited) for item in value]
                    else:
                        result[attr.key] = value.to_dict(include_relationships=False, visited=visited)
    
            return result

def get_db() -> Session: # type: ignore
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()