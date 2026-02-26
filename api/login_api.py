from core.base_api import BaseAPI
from core.base_api import APIMethod
class LoginAPI(BaseAPI):
    def __init__(self, request_context, email:str, password:str):
        super().__init__(request_context)
        self.access_token = None
        self.email = email
        self.password = password
        self.endpoint = "/api/login"
    
    def send_request(self):
        response = self._send_request(
            APIMethod.POST,
            self.endpoint,
            data={
                "email": f"{self.email}",
                "password": f"{self.password}"
                 })
        self.response_code = response.status
        self.response_json = self._get_response_body(response)

    def validate_response(self):
        print(f"\\n[DEBUG] Status code: {self.response_code}")
        print(f"[DEBUG] Response body: {self.response_json}")
        self._verify_status_code(self.response_code, 200)
        expected_schema = {
                "type": "object",
                "properties": {
                    "msg": {
                    "type": "string"
                    },
                    "accessToken": {
                    "type": "string"
                    },
                    "exp": {
                    "type": "string"
                    }
                },
                "required": [
                    "msg",
                    "accessToken",
                    "exp"
                ],
                "additionalProperties": False
}          
        self._validate_json_schema(self.response_json, expected_schema)

    def verify_login_successfully(self):
        assert self.response_json.get("accessToken") 

    def get_access_token(self):
        return self.response_json.get("accessToken")