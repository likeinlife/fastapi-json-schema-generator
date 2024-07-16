import uuid

from fastapi import status
from fastapi.testclient import TestClient


def test_fetch_state(client: TestClient, created_app: uuid.UUID):
    endpoint = f"/api/v1/format/{created_app!s}/state"
    response = client.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "NEW"
