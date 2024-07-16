import uuid

from fastapi import status
from fastapi.testclient import TestClient


def test_update_state(client: TestClient, created_app: uuid.UUID):
    endpoint = f"/api/v1/format/{created_app!s}/state"
    query = {"state": "RUNNING"}
    response = client.patch(endpoint, params=query)
    assert response.status_code == status.HTTP_200_OK, response.json()

    endpoint = f"/api/v1/format/{created_app!s}/state"
    response = client.get(endpoint)
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert response.json() == "RUNNING"
