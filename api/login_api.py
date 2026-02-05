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
            data={"email": self.email, "password": self.password})
        self.respnse_code = response.status_code,
        self.response_json = self._get_response_body(response)

    def validate_response(self):
        self._verify_status_code(self.respnse_code, 200)
        expected_schema = {
            {
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
        }    
        self._validate_json_schema(self.response_json, expected_schema)

        def verify_login_successfully(self):
            assert self.response_json["access_token"] is not None
            