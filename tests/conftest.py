"""Test configuration for CSPM Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "cspm-agent", "category": "Security AI"}
