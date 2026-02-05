import pytest
from api.me_api import MeAPI
from api.login_api import LoginAPI
from config.config import Config

# Giả sử bạn đã có fixture 'playwright_request_context' từ conftest.py
# Nếu chưa thì cần tạo, nhưng ở đây mình ví dụ cách gọi hàm.

def test_get_me_profile_successfully(playwright_request_context):
    # 1. Cần login trước để lấy token
    login_api = LoginAPI(playwright_request_context, Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD)
    login_api.send_request()
    login_api.validate_response()
    
    # Lấy token từ login response
    token = login_api.response_json["access_token"]
    
    # 2. Khởi tạo MeAPI với token vừa lấy được
    me_api = MeAPI(playwright_request_context, token)
    
    # 3. Gọi hàm gửi request
    me_api.send_request()
    
    # 4. Gọi hàm validate schema và status code
    me_api.validate_response()
    
    # 5. Gọi hàm verify_info_user để kiểm tra từng trường cụ thể
    # Ví dụ: kiểm tra email có đúng là email đã login không
    me_api.verify_info_user("email", Config.TEST_USER_EMAIL)
    
    # Ví dụ: kiểm tra id (nếu biết trước)
    # me_api.verify_info_user("id", "12345")
    
    # Ví dụ: kiểm tra tên
    # me_api.verify_info_user("name", "Test User")
