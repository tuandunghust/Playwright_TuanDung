from api.me_api import MeAPI
from api.login_api import LoginAPI
from utils.data import EMAIL, PASSWORD

class TestGetInforUser:
    email_user = EMAIL
    password_user = PASSWORD
    access_token = None

    def test_1_login(self, request_context):
        login_api = LoginAPI(request_context, TestGetInforUser.email_user, TestGetInforUser.password_user)
        login_api.send_request()
        login_api.validate_response()
        login_api.verify_login_successfully()
        TestGetInforUser.access_token = login_api.get_access_token()

    def test_2_get_infor_user(self, request_context):
        me_api  = MeAPI(request_context, TestGetInforUser.access_token)
        me_api.send_request()
        me_api.validate_response()
        me_api.verify_info_user("email", TestGetInforUser.email_user)