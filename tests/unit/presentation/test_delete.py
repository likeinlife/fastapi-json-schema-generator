import uuid

from fastapi import status
from fastapi.testclient import TestClient


def test_delete_ok(client: TestClient, created_app: uuid.UUID):
    endpoint = f"/api/v1/format/{created_app!s}"
    response = client.delete(endpoint)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    endpoint = f"/api/v1/format/{created_app!s}"
    response = client.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_not_found(client: TestClient):
    endpoint = f"/api/v1/format/{uuid.uuid4()!s}"
    response = client.delete(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
