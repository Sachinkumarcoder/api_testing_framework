POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    }
}

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email", "phone", "website",
                 "address", "company"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "phone": {"type": "string"},
        "website": {"type": "string"},
        # Address ka poora structure
        "address": {
            "type": "object",
            "required": ["street", "suite", "city", "zipcode", "geo"],
            "properties": {
                "street": {"type": "string"},
                "suite": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"},
                "geo": {
                    "type": "object",
                    "required": ["lat", "lng"],
                    "properties": {
                        "lat": {"type": "string"},
                        "lng": {"type": "string"}
                    }
                }
            }
        },
        # Company ka poora structure
        "company": {
            "type": "object",
            "required": ["name", "catchPhrase", "bs"],
            "properties": {
                "name": {"type": "string"},
                "catchPhrase": {"type": "string"},
                "bs": {"type": "string"}
            }
        }
    }
}

TODO_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "completed"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    }
}