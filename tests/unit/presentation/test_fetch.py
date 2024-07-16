import uuid
from uuid import UUID

from fastapi import status
from fastapi.testclient import TestClient


def test_fetch_ok(client: TestClient, created_app: UUID):
    endpoint = f"/api/v1/format/{created_app!s}"
    response = client.get(endpoint)
    assert response.status_code == status.HTTP_200_OK


def test_fetch_not_found(client: TestClient):
    endpoint = f"/api/v1/format/{uuid.uuid4()!s}"
    response = client.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
