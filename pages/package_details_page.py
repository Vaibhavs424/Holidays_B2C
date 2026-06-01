from playwright.sync_api import Page
from pages.base_page import BasePage


class PackageDetailsPage(BasePage):
    BOOK_PACKAGE_BUTTON = 'button[name="Book This Package"]'
    ADD_TO_CART_BUTTON = 'button[name="Add to Cart"]'
    VIEW_CART_BUTTON = 'button[name="View Cart"]'
    REQUEST_CALLBACK_BUTTON = 'button[name="Request Callback"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def click_book_package(self):
        self.page.get_by_role("button", name="Book This Package").click()

    def click_add_to_cart(self):
        self.page.get_by_role("button", name="Add to Cart").click()

    def click_view_cart(self):
        self.page.get_by_role("button", name="View Cart").click()

    def click_request_callback(self):
        self.page.get_by_role("button", name="Request Callback").click()

    def fill_callback_form(self, name: str, email: str, mobile: str, country: str, state: str, city: str):
        self.page.get_by_placeholder("Your Name").fill(name)
        self.page.get_by_placeholder("Email ID").fill(email)
        self.page.get_by_placeholder("Mobile Number").fill(mobile)
        self.page.get_by_role("textbox", name="Country *").fill(country)
        self.page.get_by_role("textbox", name="State *").fill(state)
        self.page.get_by_role("textbox", name="City *").fill(city)
