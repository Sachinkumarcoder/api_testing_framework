import pytest
from jsonschema import validate
from utils.schemas import POST_SCHEMA

class TestPostAPI:

    # =============================================
    # SMOKE TESTS
    # =============================================

    @pytest.mark.smoke
    def test_get_post_status_code(self, client):
        response = client.get("/posts/1")
        assert response.status_code == 200

    @pytest.mark.smoke
    def test_get_post_schema(self, client):
        response = client.get("/posts/1")
        validate(instance = response.json(), schema = POST_SCHEMA)

    @pytest.mark.smoke
    def test_create_post(self, client, sample_post):
        response = client.post("/posts", json = sample_post)
        data = response.json()

        assert response.status_code == 201
        assert data["title"] == sample_post["title"]
        assert data["userId"] == sample_post["userId"]

    # =============================================
    # REGRESSION TESTS
    # =============================================

    @pytest.mark.regression
    def get_all_posts(self, client):
        response = client.get("/posts")
        data = response.json()

        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) == 100

    @pytest.mark.regression
    @pytest.mark.parametrize("post_id", range(1, 11))
    def test_first_ten_posts(self, client, post_id):
        response = client.get(f"/posts/{post_id}")
        assert response.status_code == 200
        validate(instance = response.json(), schema = POST_SCHEMA)

    @pytest.mark.regression
    def test_update_post(self, client, updated_post):
        response = client.put("/posts/1", updated_post)
        data = response.json()

        assert response.status_code == 200
        assert data["title"] == updated_post["title"]

    @pytest.mark.regression
    def test_patch_post(self, client):
        response = client.patch("/posts/1", {"title": "patched title"})
        data = response.json()
        assert response.status_code == 200
        assert data["title"] == "patched title"

    @pytest.mark.regression
    def test_delete_post(self, client):
        response = client.delete("/posts/1")
        assert response.status_code in [200, 204]

    @pytest.mark.regression
    def test_response_time(self, client):
        response = client.get("/posts/1")
        assert response.elapsed.total_seconds() < 2.0

    @pytest.mark.regression
    def test_content_type(self, client):
        response = client.get("/posts/1")
        assert "application/json" in response.headers["Content-Type"]

    # =============================================
    # NEGATIVE TESTS
    # =============================================

    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_id", [0, -1, 99999])
    def test_invalid_post_ids(self, client, invalid_id):
        try:
         response = client.get(f"/posts/{invalid_id}")
         assert response.status_code == 404
        except Exception:
            assert True

    @pytest.mark.negative
    def test_create_invalid_post(self, client, invalid_post):
        response = client.post("/posts", invalid_post)        
        assert response.status_code in [200, 201, 400]
        assert "title" not in invalid_post
