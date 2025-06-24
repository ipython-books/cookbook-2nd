"""Shared pytest fixtures and configuration for the test suite."""

import os
import shutil
import tempfile
from pathlib import Path
from typing import Generator, Any

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for testing.
    
    Yields:
        Path: Path to the temporary directory.
    """
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Create a temporary file for testing.
    
    Args:
        temp_dir: The temporary directory fixture.
        
    Yields:
        Path: Path to the temporary file.
    """
    temp_file = temp_dir / "test_file.txt"
    temp_file.write_text("test content")
    yield temp_file


@pytest.fixture
def mock_config() -> dict[str, Any]:
    """Provide a mock configuration dictionary.
    
    Returns:
        dict: Mock configuration settings.
    """
    return {
        "debug": True,
        "verbose": False,
        "output_dir": "/tmp/output",
        "max_retries": 3,
        "timeout": 30,
    }


@pytest.fixture
def sample_data() -> dict[str, Any]:
    """Provide sample data for testing.
    
    Returns:
        dict: Sample data structure.
    """
    return {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
        ],
        "projects": [
            {"id": 1, "name": "Project A", "status": "active"},
            {"id": 2, "name": "Project B", "status": "completed"},
        ],
    }


@pytest.fixture
def mock_notebook_data() -> dict[str, Any]:
    """Provide mock Jupyter notebook data.
    
    Returns:
        dict: Mock notebook structure.
    """
    return {
        "cells": [
            {
                "cell_type": "code",
                "source": "print('Hello, World!')",
                "metadata": {},
                "outputs": [],
            },
            {
                "cell_type": "markdown",
                "source": "# Test Notebook\nThis is a test.",
                "metadata": {},
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


@pytest.fixture(autouse=True)
def reset_environment():
    """Reset environment variables before each test."""
    original_env = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def capture_logs(caplog):
    """Fixture to capture log messages during tests.
    
    Args:
        caplog: pytest's built-in log capture fixture.
        
    Returns:
        The caplog fixture configured for testing.
    """
    caplog.set_level("DEBUG")
    return caplog


@pytest.fixture(scope="session")
def test_resources_dir() -> Path:
    """Get the path to test resources directory.
    
    Returns:
        Path: Path to the test resources directory.
    """
    return Path(__file__).parent / "resources"


class MockResponse:
    """Mock HTTP response for testing."""
    
    def __init__(self, json_data=None, status_code=200, text=""):
        self.json_data = json_data
        self.status_code = status_code
        self.text = text
    
    def json(self):
        return self.json_data
    
    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP Error {self.status_code}")


@pytest.fixture
def mock_http_response():
    """Factory fixture for creating mock HTTP responses.
    
    Returns:
        Callable: Function to create MockResponse objects.
    """
    def _make_response(json_data=None, status_code=200, text=""):
        return MockResponse(json_data, status_code, text)
    return _make_response


# Markers for test categorization
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


# Hooks for test execution
def pytest_runtest_setup(item):
    """Run before each test method."""
    if "slow" in item.keywords and not item.config.getoption("--runslow"):
        pytest.skip("need --runslow option to run slow tests")


def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--runslow",
        action="store_true",
        default=False,
        help="run slow tests"
    )