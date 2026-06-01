from playwright.sync_api import Page
from pages.base_page import BasePage
from config import BASE_URL


class HomePage(BasePage):
    HOME_URL = BASE_URL
    MENU_BUTTON = ".sr-only"
    SEARCH_BUTTON = 'button[name="Search"]'
    PACKAGE_FILTER = "div.flex.flex-col.gap-4 article"
    SEARCH_INPUT = 'input[placeholder="Type package name…"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def navigate_to_home(self):
        self.goto(self.HOME_URL)

    def click_menu(self):
        self.click(self.MENU_BUTTON)

    def click_search(self):
        self.page.get_by_role("button", name="Search").click()

    def search_package(self, package_name: str):
        self.page.get_by_placeholder("Type package name…").fill(package_name)

    def get_package_count(self) -> int:
        return self.page.locator(self.PACKAGE_FILTER).count()

    def get_all_packages_text(self) -> list:
        return self.page.locator(self.PACKAGE_FILTER).all_text_contents()

    def verify_home_page_visible(self) -> bool:
        return self.is_visible(".bg-background")

    def select_package_by_name(self, package_name: str):
        self.page.locator(self.PACKAGE_FILTER).filter(has_text=package_name).get_by_role("button", name="View Details").click()

    def click_view_details_first_package(self):
        self.page.locator(self.PACKAGE_FILTER).nth(0).get_by_role("button", name="View Details").click()
