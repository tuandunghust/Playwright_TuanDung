import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def request_context(initial_playwright):
    request_context = initial_playwright.request.new_context(
        base_url="https://book.anhtester.com",
        extra_http_headers= {
            "Content-Type": "application/json"
        }
    )
    yield request_context

    request_context.dispose()

@pytest.fixture(scope="session")
def initial_playwright():
    playwright = sync_playwright().start()
    
    yield playwright
    
    playwright.stop()
