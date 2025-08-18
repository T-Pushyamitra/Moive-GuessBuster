from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.settings import Base, get_db
from src.main import app
from fastapi.testclient import TestClient
import pytest

# Create new in-memory DB for tests
__DATABASE_URL = "postgresql+psycopg://user:pass@localhost:52004/db"  # Replace with your actual DB

__engine = create_engine(
    __DATABASE_URL
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=__engine)

# Override DB dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    print("TEST")
    Base.metadata.drop_all(bind=__engine)
    Base.metadata.create_all(bind=__engine)

    with TestClient(app) as c:
        yield c

    