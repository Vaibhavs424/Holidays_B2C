from playwright.sync_api import Page
from pages.base_page import BasePage


class RequestCallbackPage(BasePage):
    REQUEST_CALLBACK_BUTTON = "Request Callback"
    NAME_PLACEHOLDER = "Your Name"
    EMAIL_PLACEHOLDER = "Email ID"
    MOBILE_PLACEHOLDER = "Mobile Number"
    COUNTRY_SELECT_TEXT = "Select Country"
    COUNTRY_SEARCH_PLACEHOLDER = "Search country..."
    STATE_SELECT_TEXT = "Select State"
    STATE_SEARCH_PLACEHOLDER = "Search state..."
    CITY_ROLE_NAME = "City *"
    SUBMIT_BUTTON = "Submit"

    def __init__(self, page: Page):
        super().__init__(page)

    def click_request_callback(self):
        self.page.get_by_role("button", name=self.REQUEST_CALLBACK_BUTTON).click()

    def fill_callback_form(self, name: str, email: str, mobile: str, country: str, state: str, city: str):
        self.page.get_by_placeholder(self.NAME_PLACEHOLDER).fill(name)
        self.page.get_by_placeholder(self.EMAIL_PLACEHOLDER).fill(email)
        self.page.get_by_placeholder(self.MOBILE_PLACEHOLDER).fill(mobile)
        self.page.get_by_text(self.COUNTRY_SELECT_TEXT).click()
        self.page.get_by_placeholder(self.COUNTRY_SEARCH_PLACEHOLDER).fill(country)
        self.page.get_by_role("option", name=country).click()
        self.page.get_by_text(self.STATE_SELECT_TEXT).click()
        self.page.get_by_placeholder(self.STATE_SEARCH_PLACEHOLDER).fill(state)
        self.page.get_by_role("option", name=state).click()
        self.page.get_by_role("textbox", name=self.CITY_ROLE_NAME).fill(city)

    def submit_callback_request(self):
        self.page.get_by_role("button", name=self.SUBMIT_BUTTON).click()
