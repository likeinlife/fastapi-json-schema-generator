from uuid import UUID, uuid4

from fastapi import status
from fastapi.testclient import TestClient


def test_create(client: TestClient):
    endpoint = "/api/v1/format/"
    payload = {
        "kind": "string",
        "name": "string",
        "version": "string",
        "description": "string",
        "configuration": {
            "specification": {"param_a": str(uuid4())},
            "settings": {"param_b": str(uuid4())},
        },
    }
    response = client.post(endpoint, json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert UUID(response.json())
