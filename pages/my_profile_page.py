from core.base_page import BasePage

class MyProfilePage(BasePage):
    # Locators
    NAME_INPUT = "input[name='name']"
    PHONE_INPUT = "input[name='phone']"
    ADDRESS_INPUT = "textarea[name='address']"
    SAVE_BUTTON = "button[type='submit']"
    SUCCESS_MESSAGE = ".alert-success"
    
    def navigate_to_profile(self):
        self.navigate("/my-profile")
    
    def update_profile_ui(self, name, phone, address):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.PHONE_INPUT, phone)
        self.fill(self.ADDRESS_INPUT, address)
        self.click(self.SAVE_BUTTON)
    
    def get_profile_info(self):
        return {
            "name": self.page.input_value(self.NAME_INPUT),
            "phone": self.page.input_value(self.PHONE_INPUT),
            "address": self.page.input_value(self.ADDRESS_INPUT)
        }
    
    def verify_update_success(self):
        return self.is_visible(self.SUCCESS_MESSAGE)
