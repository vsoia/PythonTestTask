import pytest
import requests
from playwright.sync_api import sync_playwright

API_KEY = "reqres_9dfd5357c8124ea4b8fe8d61ad016f70"

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    })
    yield s
    s.close()


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()