import pytest
from pages.my_profile_page import MyProfilePage

class TestUIIndependent:
    
    def test_update_profile_ui(self, page):
        """
        Verify updating profile via UI (independently).
        """
        my_profile = MyProfilePage(page)
        my_profile.navigate_to_profile()
        
        # Test Data
        new_name = "UI Updated Name"
        new_phone = "0999999999"
        new_addr = "Hanoi, Vietnam"
        
        my_profile.update_profile_ui(new_name, new_phone, new_addr)
        
        # Verification on UI
        assert my_profile.verify_update_success()
        info = my_profile.get_profile_info()
        assert info['name'] == new_name
