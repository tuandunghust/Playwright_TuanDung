from core.base_api import BaseAPI
from core.base_api import APIMethod

class ProfileAPI(BaseAPI):
    def __init__(self, request_context, access_token: str):
        super().__init__(request_context)
        self.endpoint = "/api/profile"
        self.access_token = access_token
        self.key_profile = ["id", "name", "email", "avatarUrl", "phone", "address"]
      
    def change_password(self, old_password: str, new_password: str):
        response = self._send_request(
            APIMethod.PATCH,
            self.endpoint,
            data={"password": f"{old_password}", "newPassword": f"{new_password}"},
            headers={"Authorization": f"Bearer {self.access_token}"}
        )
        self.response_code = response.status_code
        self.response_json = self._get_response_body(response)

    def validate_response(self):
        self._verify_status_code(self.response_code, 200)
        expected_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "email": {"type": "string"},
                "avatarUrl": {"type": "string"},
                "phone": {"type": "string"},
                "address": {"type": "string"},
                "config": {}
            },
            "required": [
                "id",
                "name",
                "email",
                "avatarUrl",
                "phone",
                "address"
            ],
            "additionalProperties": False
        }    
        self._validate_json_schema(self.response_json, expected_schema) 

    def update_profile(self, infomation_change: dict):  
        response = self._send_request(
            APIMethod.PATCH,
            self.endpoint,
            data=infomation_change,
            headers={"Authorization": f"Bearer {self.access_token}"}
        )
        self.response_code = response.status_code
        self.response_json = self._get_response_body(response)
    
    def verify_update_profile_successfully(self):
        assert self.response_json["msg"] == "Updated profile successfully."