import pytest
import httpx

# Define an async fixture using httpx.AsyncClient
@pytest.fixture
async def async_client():
    async with httpx.AsyncClient(base_url="https://httpbin.org") as client:
        yield client

# Write your async test
async def test_external_api(async_client):
    response = await async_client.get("/get")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert "url" in data


# httpx.AsyncClient is an async-compatible HTTP client.
# Using it as a context manager (async with) ensures connections are properly opened and cleaned up.

