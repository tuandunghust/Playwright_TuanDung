from api.me_api import MeAPI
from api.login_api import LoginAPI
from api.profile_api import ProfileAPI
from utils.data import EMAIL, PASSWORD

class TestUpdateProfile:
    email_user = EMAIL
    password_user = PASSWORD
    access_token = None
    information_change = {
        "name": "Test User",
        "phone": "1234567890",
        "address": "Test Address"
    }
    information_change_unsuccessfully = {
        "name": "Test User",
        "phone": "1234567890",
        "address": "Test Address"
    }

    def test_1_login(self, request_context):
        login_api = LoginAPI(request_context, TestUpdateProfile.email_user, TestUpdateProfile.password_user)
        login_api.send_request()
        login_api.validate_response()
        login_api.verify_login_successfully()
        TestUpdateProfile.access_token = login_api.get_access_token()

    def test_2_update_profile_successfully(self, request_context):
        profile_api  = ProfileAPI(request_context, TestUpdateProfile.access_token)
        profile_api.update_profile(TestUpdateProfile.information_change)
        profile_api.validate_response()
        profile_api.verify_update_profile_successfully()
    
    def test_3_update_profile_unsuccessfully(self, request_context):
        profile_api  = ProfileAPI(request_context, TestUpdateProfile.access_token)
        profile_api.update_profile(TestUpdateProfile.information_change_unsuccessfully)
        profile_api.validate_response()
        profile_api.verify_update_profile_successfully()

        