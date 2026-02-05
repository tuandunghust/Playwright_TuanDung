import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def api_context():
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url="https://book.anhtester.com",
            extra_http_headers={
                "Accept": "application/json"
            }
        )
        yield request_context
        request_context.dispose()
​
