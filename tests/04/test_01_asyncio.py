import asyncio
import pytest

@pytest.mark.asyncio
async def test_async_feature():
    await asyncio.sleep(0.1)
    result = 42
    assert result == 42