import pytest
from pages.settings_page import SettingsPage

class TestTheme:
    
    @pytest.mark.parametrize("theme", ["light", "dark", "system"])
    def test_change_theme_persisted(self, page, theme):
        """
        Change theme -> Reload -> Verify persisted
        """
        settings = SettingsPage(page)
        settings.navigate_to_settings()
        
        # Change Theme
        settings.change_theme(theme)
        
        # Reload Page
        page.reload()
        
        # Verify persistence
        current_theme = settings.get_current_theme()
        assert current_theme == theme
