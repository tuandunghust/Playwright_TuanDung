from core.base_page import BasePage

class SettingsPage(BasePage):
    THEME_SELECT = "select[name='theme']"
    
    def navigate_to_settings(self):
        self.navigate("/settings")
        
    def change_theme(self, theme_value):
        # theme_value: 'light', 'dark', 'system'
        self.page.select_option(self.THEME_SELECT, theme_value)
    
    def get_current_theme(self):
        return self.page.input_value(self.THEME_SELECT)
