from core.base_api import BaseAPI
from core.base_api import APIMethod

class ProfileAPI(BaseAPI):
    def __init__(self, request_context, access_token: str):
        super().__init__(request_context)
        self.endpoint = "/api/profile"
        self.access_token = access_token
        self.key_profile = ["id", "name", "email", "avatarUrl", "phone", "address"]
        self.response_code = None
        self.response_json = None
      
    def change_password(self, old_password: str, new_password: str):
        print(f"\n[DEBUG] PATCH {self.endpoint} (Change Password)")
        print(f"[DEBUG] Payload: { {'fields': {'password': '{old_password}', 'newPassword': '{new_password}'}}}")
        response = self._send_request(
            APIMethod.PATCH,
            self.endpoint,
            data={"fields": {"password": f"{old_password}", "newPassword": f"{new_password}"}},
            headers={"Authorization": f"Bearer {self.access_token}"}
        )
        self.response_code = response.status
        self.response_json = self._get_response_body(response)
        print(f"[DEBUG] Status: {self.response_code}")
        print(f"[DEBUG] Body: {self.response_json}")

    def validate_response(self):
        self._verify_status_code(self.response_code, 200)
        expected_schema = {
            "type": "object",
            "properties": {
                "msg": {
                    "type": "string"
                }
            },
            "required": [
                "msg"
            ]
        }
        self._validate_json_schema(self.response_json, expected_schema)
    
    def update_profile(self, information_change: dict): 
        for key in information_change.keys():
            if key not in self.key_profile:
                raise ValueError(f"Key '{key}' is not valid. Valid keys are: {self.key_profile}")
  
        response = self._send_request(
            APIMethod.PATCH,
            self.endpoint,
            data=information_change,
            headers={"Authorization": f"Bearer {self.access_token}"}
        )
        self.response_code = response.status
        self.response_json = self._get_response_body(response)

    def validate_update_profile_successfully(self):
        self._verify_status_code(self.response_code, 200)
        assert self.response_json["msg"] == "Updated profile successfully."

    def validate_error_response(self, expected_code: int):
        self._verify_status_code(self.response_code, expected_code)
        # Linh hoạt kiểm tra msg hoặc error cho các trường hợp lỗi
        assert "msg" in self.response_json or "error" in self.response_json