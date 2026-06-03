import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="chromium",
        help="Browser to run tests on: chromium, firefox, or webkit"
    )


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser-name")


@pytest.fixture
def page(browser_name):
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)

        context = browser.new_context(
            # viewport={"width": 1920, "height": 1080}
        )

        page = context.new_page()
        page.set_default_timeout(60000)

        yield page

        page.screenshot(path="last_page.png")

        context.close()
        browser.close()
