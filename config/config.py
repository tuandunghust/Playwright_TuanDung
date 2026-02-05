import os

class Config:
    # Base URLs - Update these with actual environment URLs
    BASE_URL = os.getenv("BASE_URL", "https://automation-practice.example.com") 
    API_URL = os.getenv("API_URL", "https://api.automation-practice.example.com")
    
    # Timeouts
    TIMEOUT = 10000  # 10 seconds default wait
    
    # Test Accounts
    TEST_USER_EMAIL = os.getenv("TEST_EMAIL", "testuser@example.com")
    TEST_USER_PASSWORD = os.getenv("TEST_PASSWORD", "SecretPass123")
    
    # API Endpoints
    LOGIN_ENDPOINT = "/auth/login"
    PROFILE_ENDPOINT = "/api/me"
    UPDATE_PROFILE_ENDPOINT = "/api/profile"
