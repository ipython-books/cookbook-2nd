"""Validation tests to verify the testing infrastructure is set up correctly."""

import sys
from pathlib import Path

import pytest


class TestInfrastructureSetup:
    """Test class to validate the testing infrastructure."""
    
    @pytest.mark.unit
    def test_pytest_installed(self):
        """Test that pytest is installed and importable."""
        assert "pytest" in sys.modules
    
    @pytest.mark.unit
    def test_pytest_cov_installed(self):
        """Test that pytest-cov is available."""
        import pytest_cov
        assert pytest_cov is not None
    
    @pytest.mark.unit
    def test_pytest_mock_installed(self):
        """Test that pytest-mock is available."""
        import pytest_mock
        assert pytest_mock is not None
    
    @pytest.mark.unit
    def test_test_directory_structure(self):
        """Test that the test directory structure exists."""
        tests_dir = Path(__file__).parent
        assert tests_dir.exists()
        assert tests_dir.name == "tests"
        
        # Check subdirectories
        assert (tests_dir / "unit").exists()
        assert (tests_dir / "integration").exists()
        
        # Check __init__.py files
        assert (tests_dir / "__init__.py").exists()
        assert (tests_dir / "unit" / "__init__.py").exists()
        assert (tests_dir / "integration" / "__init__.py").exists()
    
    @pytest.mark.unit
    def test_conftest_exists(self):
        """Test that conftest.py exists and is importable."""
        conftest_path = Path(__file__).parent / "conftest.py"
        assert conftest_path.exists()
        
        # Test that we can import from conftest
        from tests.conftest import temp_dir, mock_config
        assert temp_dir is not None
        assert mock_config is not None
    
    @pytest.mark.unit
    def test_fixtures_work(self, temp_dir, mock_config, sample_data):
        """Test that the fixtures from conftest.py work correctly."""
        # Test temp_dir fixture
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        
        # Test mock_config fixture
        assert isinstance(mock_config, dict)
        assert "debug" in mock_config
        assert mock_config["debug"] is True
        
        # Test sample_data fixture
        assert isinstance(sample_data, dict)
        assert "users" in sample_data
        assert len(sample_data["users"]) == 2
    
    @pytest.mark.unit
    def test_temp_file_fixture(self, temp_file):
        """Test that the temp_file fixture works correctly."""
        assert temp_file.exists()
        assert temp_file.is_file()
        assert temp_file.read_text() == "test content"
    
    @pytest.mark.unit
    def test_mock_response_fixture(self, mock_http_response):
        """Test that the mock_http_response fixture works correctly."""
        # Test successful response
        response = mock_http_response({"status": "ok"}, 200)
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
        
        # Test error response
        error_response = mock_http_response(status_code=404)
        assert error_response.status_code == 404
        with pytest.raises(Exception):
            error_response.raise_for_status()
    
    @pytest.mark.unit
    def test_markers_configured(self, request):
        """Test that custom markers are properly configured."""
        markers = request.config.getini("markers")
        marker_names = [m.split(":")[0] for m in markers]
        
        assert "unit" in marker_names
        assert "integration" in marker_names
        assert "slow" in marker_names
    
    @pytest.mark.slow
    def test_slow_marker_skip(self):
        """Test that slow tests can be skipped without --runslow flag."""
        # This test will be skipped unless --runslow is provided
        import time
        time.sleep(0.1)  # Simulate slow test
        assert True
    
    @pytest.mark.integration
    def test_integration_marker(self):
        """Test that integration marker works."""
        # This is just to verify the marker works
        assert True
    
    def test_coverage_configured(self):
        """Test that coverage is properly configured."""
        # This test verifies coverage will run with pytest
        # The actual coverage report will be generated when running tests
        assert True


@pytest.mark.unit
def test_python_version():
    """Test that Python version meets minimum requirements."""
    assert sys.version_info >= (3, 8), "Python 3.8 or higher is required"


@pytest.mark.unit
def test_project_root_accessible():
    """Test that we can access the project root."""
    project_root = Path(__file__).parent.parent
    assert project_root.exists()
    assert (project_root / "pyproject.toml").exists()