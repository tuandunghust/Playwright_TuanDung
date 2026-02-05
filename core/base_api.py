from enum import Enum
from playwright.sync_api import Response
from jsonschema import validate
class APIMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    
class BaseAPI:
    def __init__(self, request_context):
        self.request_context = request_context

    def _send_request(self, method: APIMethod, endpoint: str, data=None, headers=None):
        if method == APIMethod.GET:
            response = self.request_context.get(endpoint, headers=headers)
        elif method == APIMethod.POST:
            response = self.request_context.post(endpoint, data=data, headers=headers)
        elif method == APIMethod.PUT:
            response = self.request_context.put(endpoint, data=data, headers=headers)
        elif method == APIMethod.DELETE:
            response = self.request_context.delete(endpoint, data=data, headers=headers)
        elif method == APIMethod.PATCH:
            response = self.request_context.patch(endpoint, data=data, headers=headers)

        return response

    def _verify_status_code(self, response_code: int, expected_status_code: int):
        assert response_code == expected_status_code

    def _get_response_body(self, response: Response):
        response_body = response.json()
        return response_body

    def _validate_json_schema(self, response_body, expect_schema: dict):
        try:
            validate(instance=response_body, schema=expect_schema)
        except Exception as e:
            raise AssertionError(f"JSON schema validation failed: {str(e)}")
