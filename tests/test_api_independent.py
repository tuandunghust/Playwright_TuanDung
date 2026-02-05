import pytest
from api.profile_api import ProfileAPI

class TestAPIIndependent:
    
    @pytest.fixture
    def profile_api(self, auth_token):
        return ProfileAPI(auth_token)

    def test_get_profile_api(self, profile_api):
        """
        Verify API returns profile data correctly.
        """
        response = profile_api.get_profile()
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "email" in data
