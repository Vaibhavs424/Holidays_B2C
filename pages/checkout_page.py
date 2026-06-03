from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    EMAIL_PLACEHOLDER = 'input[placeholder="you@example.com"]'
    PASSWORD_PLACEHOLDER = 'input[placeholder="Min. 8 characters"]'
    SIGN_IN_BUTTON = 'button[name="Sign In"]'
    FIRST_NAME_TEXTBOX = 'textbox[name="First name"]'
    LAST_NAME_TEXTBOX = 'textbox[name="Last name"]'
    EMAIL_TEXTBOX = 'textbox[name="email"]'
    MOBILE_TEXTBOX = 'textbox[name="Mobile"]'
    PROCEED_TO_PAY_BUTTON = 'button[name="Proceed to Pay"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def enter_sign_in_email(self, email: str):
        self.page.get_by_placeholder("you@example.com").fill(email)

    def enter_sign_in_password(self, password: str):
        self.page.get_by_placeholder("Min. 8 characters").fill(password)

    def click_sign_in(self):
        self.page.get_by_role("button", name="Sign In").nth(1).click()

    def enter_first_name(self, first_name: str):
        self.page.get_by_role("textbox", name="First name").fill(first_name)

    def enter_last_name(self, last_name: str):
        self.page.get_by_role("textbox", name="Last name").fill(last_name)

    def enter_email(self, email: str):
        self.page.get_by_role("textbox", name="email").fill(email)

    def enter_mobile(self, mobile: str):
        self.page.get_by_role("textbox", name="Mobile").fill(mobile)

    def click_proceed_to_pay(self):
        proceed_button = self.page.get_by_role("button", name="Proceed to Pay")
        proceed_button.wait_for(state="visible", timeout=30000)
        proceed_button.scroll_into_view_if_needed()
        proceed_button.click()

    def fill_checkout_form(self, first_name: str, last_name: str, email: str, mobile: str):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_mobile(mobile)
