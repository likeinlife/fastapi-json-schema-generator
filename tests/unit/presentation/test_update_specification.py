import uuid

from fastapi import status
from fastapi.testclient import TestClient


def test_update_specification(client: TestClient, created_app: uuid.UUID):
    endpoint = f"/api/v1/format/{created_app!s}/specification"
    payload = {"param_a": str(uuid.uuid4())}
    response = client.patch(endpoint, json=payload)
    assert response.status_code == status.HTTP_200_OK, response.json()

    endpoint = f"/api/v1/format/{created_app!s}"
    response = client.get(endpoint)
    assert response.status_code == status.HTTP_200_OK, response.json()
    assert response.json()["specification"] == payload
