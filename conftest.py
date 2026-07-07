import pytest
from utils.api_client import APIClient

# =============================================
# FIXTURE 1: API Client
# =============================================

@pytest.fixture(scope="session")
def client():
    api = APIClient()
    yield api
    api.close()

# =============================================
# FIXTURE 2: Sample Post Data
# =============================================

@pytest.fixture
def sample_post():
    return {
        "title": "Automation test post",
        "body": "Body of test post",
        "userId": 1
    }

# =============================================
# FIXTURE 3: Invalid Post Data
# =============================================

@pytest.fixture
def invalid_post():
    return {
        "body": "Body of test post",
        "userId": 1
    }

# =============================================
# FIXTURE 4: Sample User Data
# =============================================

@pytest.fixture
def sample_user(client):
    response = client.get("/users/1")
    return response.json()

# =============================================
# FIXTURE 5: Updated Post Data
# =============================================

@pytest.fixture
def updated_post():
    return {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }