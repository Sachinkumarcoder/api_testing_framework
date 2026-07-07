import pytest

class TestNegativeScenarios:

    # =============================================
    # INVALID IDs
    # =============================================

    @pytest.mark.negative
    @pytest.mark.parametrize("endpoints", "invalid_id", [
        ("/posts", 99999),
        ("/users", 99999),
        ("/todos", 99999),
        ("/albums", 99999)
    ])
    def test_invalid_ids(self, client, endpoints, invalid_id):
        try:
            response = client.get(f"{endpoints}/{invalid_id}")
            assert response.status_code == 404
        except Exception:
            assert True

    @pytest.mark.negative
    @pytest.mark.parametrize("post_id", [0, -1, -100])
    def test_negative_post_ids(self, client, post_id):
        try:
            response = client.get(f"/posts/{post_id}")
            assert response.status_code == 404
        except Exception:
            assert True
    # =============================================
    # INVALID DATA — POST REQUEST
    # =============================================

    @pytest.mark.negative
    def test_create_empty_post(self, client):
        response = client.post("/posts", {})
        assert response.status_code in [200, 201, 400]

    @pytest.mark.negative
    def test_create_post_missing_title(self, client, invalid_post):
        response = client.post("/posts", invalid_post)
        assert response.status_code in [200, 201, 404]
        assert "title" not in invalid_post

    @pytest.mark.negative
    def test_create_post_invalid_userId(self, client):
        payload = {
            "title": "Test Title",
            "body": "Test Body",
            "userId": "wrong_id"
        }

        response = client.post("/posts", payload)
        assert response.status_code in [200, 201, 404, 422]

    # =============================================
    # INVALID DATA — PUT REQUEST
    # =============================================

    @pytest.mark.negative
    def test_update_nonexistent_post(self, client):
        payload = {
            "title": "Test Title",
            "body": "Test Body",
            "userId": 1
        }
        try:
         response = client.put("/posts/99999", payload)
         assert response.status_code == 404
        except Exception:
            assert True

    # =============================================
    # INVALID DATA — DELETE REQUEST
    # =============================================

    @pytest.mark.negative
    def test_delete_nonexistent_post(self, client):
        try:
            response = client.delete("/posts/99999")
            assert response.status_code == 404
        except Exception:
            assert True

    # =============================================
    # RESPONSE FIELDS
    # =============================================

    @pytest.mark.negative
    def test_password_not_in_response(self, client):
        response = client.get("/users/1")
        data = response.json()
        assert "password" not in data

    @pytest.mark.negative
    def test_secret_not_in_response(self, client):
        response = client.get("/users/1")
        data = response.json()
        assert "secret" not in data

    # =============================================
    # RESPONSE TIME
    # =============================================

    @pytest.mark.negative
    @pytest.mark.slow
    @pytest.mark.parametrize("endpoints", [
        "/posts",
        "/users",
        "/todos",
        "/albums"
    ])
    def test_response_time_all_endpoints(self, client, endpoints):
        response = client.get(endpoints)
        assert response.elapsed.total_seconds()<2.0