from core.base_api import BaseAPI
from api.login_api import LoginAPI
from api.profile_api import ProfileAPI
from utils.data import EMAIL, PASSWORD

class TestChangePassword:
    name_user = None
    email_user = EMAIL
    password_user = PASSWORD
    access_token = None
    new_password = "Abc@1234"

    def test_1_login(self, request_context):
        login_api = LoginAPI(request_context, TestChangePassword.email_user, TestChangePassword.password_user)
        login_api.send_request()
        login_api.validate_response()
        login_api.verify_login_successfully()
        TestChangePassword.access_token = login_api.get_access_token()

    def test_2_change_password(self, request_context):
        profile_api  = ProfileAPI(request_context, TestChangePassword.access_token)
        profile_api.change_password(TestChangePassword.password_user, TestChangePassword.new_password)
        profile_api.validate_response()
        profile_api.verify_update_profile_successfully()
        TestChangePassword.password_user = TestChangePassword.new_password