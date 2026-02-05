from core.base_api import BaseAPI
from config.config import Config

class ProfileAPI:
    def __init__(self, token):
        self.api = BaseAPI(Config.API_URL)
        auth_headers = {"Authorization": f"Bearer {token}"}
        self.api.set_headers(auth_headers)

    def get_profile(self):
        return self.api.get(Config.PROFILE_ENDPOINT)

    def update_profile(self, name=None, phone=None, address=None):
        payload = {}
        if name: payload['name'] = name
        if phone: payload['phone'] = phone
        if address: payload['address'] = address
        
        return self.api.patch(Config.UPDATE_PROFILE_ENDPOINT, json=payload)
