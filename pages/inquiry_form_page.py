from playwright.sync_api import Page
from pages.base_page import BasePage


class InquiryFormPage(BasePage):
    FULL_NAME_PLACEHOLDER = 'input[placeholder="Enter your full name"]'
    EMAIL_PLACEHOLDER = 'input[placeholder="you@example.com"]'
    MOBILE_PLACEHOLDER = 'input[placeholder="10-digit mobile number"]'
    DESTINATION_PLACEHOLDER = 'input[placeholder="e.g. Bali, Dubai, Kashmir"]'
    DATE_BUTTON = 'button[name="Select travel date"]'
    CALLBACK_BUTTON = 'button[name="Get Free Callback"]'
    CONTINUE_BROWSING_BUTTON = 'button[name="Continue Browsing"]'
    SUCCESS_MESSAGE = "Request Received"

    def __init__(self, page: Page):
        super().__init__(page)

    def enter_full_name(self, name: str):
        self.page.get_by_placeholder("Enter your full name").fill(name)

    def enter_email(self, email: str):
        self.page.get_by_placeholder("you@example.com").fill(email)

    def enter_mobile(self, mobile: str):
        self.page.get_by_placeholder("10-digit mobile number").fill(mobile)

    def enter_destination(self, destination: str):
        self.page.get_by_placeholder("e.g. Bali, Dubai, Kashmir").fill(destination)

    def click_select_date(self):
        self.page.get_by_role("button", name="Select travel date").click()

    def select_date_by_index(self, index: int):
        self.page.locator("tbody tr td").nth(index).click()

    def click_get_callback(self):
        self.page.get_by_role("button", name="Get Free Callback").click()

    def click_continue_browsing(self):
        self.page.get_by_role("button", name="Continue Browsing").click()

    def verify_success_message(self) -> bool:
        return self.page.get_by_text(self.SUCCESS_MESSAGE).is_visible()

    def fill_inquiry_form(self, full_name: str, email: str, mobile: str, destination: str, date_index: int):
        self.enter_full_name(full_name)
        self.enter_email(email)
        self.enter_mobile(mobile)
        self.enter_destination(destination)
        self.click_select_date()
        self.select_date_by_index(date_index)
