from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Restore in-memory data between tests to avoid cross-test pollution."""
    # Arrange
    original_activities = deepcopy(activities)

    yield

    # Assert cleanup state is restored for next test
    activities.clear()
    activities.update(deepcopy(original_activities))
