import pytest
from jsonschema import validate, ValidationError
from utils.schemas import POST_SCHEMA, USER_SCHEMA, TODO_SCHEMA

class TestSchemaValidation:

    # =============================================
    # POST SCHEMA TESTS
    # =============================================

    @pytest.mark.smoke
    def test_single_post_schema(self, client):
        response = client.get("/posts/1")
        validate(instance=response.json(), schema=POST_SCHEMA)

    
    @pytest.mark.regression
    @pytest.mark.parametrize("post_id", [1,10, 50, 100])
    def test_multiple_post_schema(self, client, post_id):
        response = client.get(f"/posts/{post_id}")
        validate(instance=response.json(), schema=POST_SCHEMA)
    
    @pytest.mark.regression
    def test_all_post_schema(self, client):
        response=client.get("/posts")
        posts = response.json()
        for post in posts:
            validate(instance=post, schema=POST_SCHEMA) 

    # =============================================
    # USER SCHEMA TESTS
    # =============================================

    @pytest.mark.smoke
    def test_single_user_schema(self, client):
        response = client.get("/users/1")
        validate(instance=response.json(), schema= USER_SCHEMA)

    @pytest.mark.regression
    @pytest.mark.parametrize("user_id", range(1, 6))
    def test_multiple_users_schema(self, client, user_id):
        response = client.get(f"/users/{user_id}")
        validate(instance=response.json(), schema=USER_SCHEMA)

    @pytest.mark.regression
    def test_all_users_schema(self, client):
        response = client.get("/users")
        users = response.json()
        for user in users:
            validate(instance=user, schema=USER_SCHEMA)

    # =============================================
    # TODO SCHEMA TESTS
    # =============================================

    @pytest.mark.smoke
    def single_todo_schema(self, client):
        response = client.get("/todos/1")
        validate(instance=response.json(), schema=TODO_SCHEMA)

    @pytest.mark.regression
    @pytest.mark.parametrize("todo_id", [1, 50, 100 , 200])
    def test_multiple_todos_schema(self, client, todo_id):
        response = client.get(f"/todos/{todo_id}")
        validate(instance=response.json(), schema=TODO_SCHEMA)

    @pytest.mark.regression
    def test_all_todo_schema(self, client):
        response = client.get("/todos")
        todos = response.json()
        for todo in todos:
            validate(instance=todo, schema=TODO_SCHEMA)

    # =============================================
    # SCHEMA VALIDATION ERROR TESTS
    # =============================================

    @pytest.mark.negative
    def test_invalid_schema_caught(self, client):
        wrong_schema = {
            "type": "object",
            "required": ["id", "title", "fake_field"],
            "properties": {
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "fake_field": {"type": "string"}
            }
        }

        response = client.get("/posts/1")
        data = response.json()

        with pytest.raises(ValidationError):
            validate(instance=data, schema=wrong_schema)

    def test_wrong_type_caught(self, client):
        wrong_type_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"}
            }
        }

        response = client.get("/posts/1")
        data = response.json()
        with pytest.raises(ValidationError):
            validate(instance=data, schema=wrong_type_schema)

    