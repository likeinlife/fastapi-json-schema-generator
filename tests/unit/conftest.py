from uuid import UUID

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from container.creators import get_container, get_memory_container
from presentation.api.main import create_app
from unit.mocks.settings import MockSettings


@pytest.fixture(scope="session", autouse=True)
def app() -> FastAPI:
    mock_settings = MockSettings()

    app = create_app(mock_settings)  # type: ignore
    app.dependency_overrides[get_container] = get_memory_container
    return app


@pytest.fixture(scope="session", autouse=True)
def client(app: FastAPI) -> TestClient:
    return TestClient(app)


@pytest.fixture()
def created_app(client: TestClient) -> UUID:
    endpoint = "/api/v1/format/"
    payload = {
        "kind": "string",
        "name": "string",
        "version": "string",
        "description": "string",
        "configuration": {"specification": {}, "settings": {}},
    }
    response = client.post(endpoint, json=payload)
    return UUID(response.json())
