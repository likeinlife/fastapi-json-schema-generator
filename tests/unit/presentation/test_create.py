from uuid import UUID

from fastapi import status
from fastapi.testclient import TestClient


def test_create(client: TestClient):
    endpoint = "/api/v1/format/"
    payload = {
        "kind": "string",
        "name": "string",
        "version": "string",
        "description": "string",
        "configuration": {"specification": {}, "settings": {}},
    }
    response = client.post(endpoint, json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert UUID(response.json())
