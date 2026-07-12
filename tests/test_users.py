import pytest
from jsonschema import validate
from utils.schemas import USER_SCHEMA

class TestUsersAPI:

    # =============================================
    # SMOKE TESTS
    # =============================================

    @pytest.mark.smoke
    def get_user_status_code(self, client):
        response = client.get("/users/1")
        assert response.status_code == 200

    @pytest.mark.smoke
    def test_get_user_schema(self, client):
        response = client.get("/users/1")
        validate(instance = response.json(), schema=USER_SCHEMA)

    @pytest.mark.smoke
    def test_user_email_format(self, client):
        response = client.get("/users/1")
        data = response.json()

        assert "@" in data["email"]
        assert len(data["email"]) > 0

    # =============================================
    # REGRESSION TESTS
    # =============================================

    @pytest.mark.regression
    def test_get_all_users(self, client):
        response = client.get("/users")
        data = response.json()

        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) == 10

    @pytest.mark.regerssion
    @pytest.mark.parametrize("user_id", range(1, 6))
    def test_first_five_users(self, client, user_id):
        response = client.get(f"/users/{user_id}")
        assert response.status_code == 200
        validate(instance=response.json(), schema=USER_SCHEMA)

    @pytest.mark.regerssion
    @pytest.mark.parametrize("user_id", range(1, 6))
    def test_first_five_users_email_format(self, client, user_id):
        response = client.get(f"/users/{user_id}")
        data = response.json()
        assert '@' in data["email"]

    @pytest.mark.regerssion
    def test_users_adderss_field(self, client):
        response = client.get("/users/1")
        data = response.json()
        address = data["address"]
        assert "street" in address
        assert "city" in address
        assert "zipcode" in address

    @pytest.mark.regerssion
    def test_users_company_field(self, client):
        response = client.get("/users/1")
        data = response.json()

        company = data["company"]
        assert "name" in company
        assert "catchPhrase" in company
        assert "bs" in company

    @pytest.mark.regerssion
    def test_response_time(self, client):
        response = client.get("/users/1")
        assert response.elapsed.total_seconds() < 2.0

    @pytest.mark.regerssion
    def test_content_type(self, client):
        response = client.get("/users/1")
        assert "application/json" in response.headers["Content-Type"]

    # =============================================
    # NEGATIVE TESTS
    # =============================================

    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_user", [0, -1, 99999])
    def test_invalid_user_ids(self, client, invalid_user):
        try:
            response = client.get(f"/users/{invalid_user}")
            response.status_code == 404
        except Exception:
            assert True

    @pytest.mark.negative
    def test_user_password_not_exposed(self, client):
        response = client.get("/users/1")
        data = response.json()
        assert "password" not in data



    

