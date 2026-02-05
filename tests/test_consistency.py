import pytest
from pages.my_profile_page import MyProfilePage
from api.profile_api import ProfileAPI
import time

class TestConsistency:

    @pytest.fixture
    def profile_api(self, auth_token):
        return ProfileAPI(auth_token)

    def test_api_changes_reflect_on_ui(self, page, profile_api):
        """
        Update Profile via API -> Verify on UI
        """
        # 1. Update via API
        api_name = "API Change Name"
        headers = profile_api.update_profile(name=api_name)
        assert headers.status_code == 200

        # 2. Open UI and Verify
        my_profile = MyProfilePage(page)
        my_profile.navigate_to_profile()
        
        # Reload to ensure fresh data if simple navigate isn't enough (depending on app cache)
        page.reload() 
        
        info = my_profile.get_profile_info()
        assert info['name'] == api_name
    
    def test_ui_changes_reflect_on_api(self, page, profile_api):
        """
        Update Profile via UI -> Verify on API
        """
        # 1. Update via UI
        ui_name = "UI Change Name"
        my_profile = MyProfilePage(page)
        my_profile.navigate_to_profile()
        my_profile.update_profile_ui(name=ui_name, phone="123", address="Test Addr")
        assert my_profile.verify_update_success()
        
        # 2. Verify via API
        response = profile_api.get_profile()
        assert response.status_code == 200
        assert response.json()['name'] == ui_name
