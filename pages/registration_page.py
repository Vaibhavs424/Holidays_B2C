from playwright.sync_api import Page
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    CREATE_ACCOUNT_BUTTON = 'button[name="Create one"]'
    NAME_PLACEHOLDER = 'input[placeholder="John Doe"]'
    EMAIL_PLACEHOLDER = 'input[placeholder="you@example.com"]'
    PASSWORD_PLACEHOLDER = 'input[placeholder="Min. 8 characters"]'
    CONFIRM_PASSWORD_PLACEHOLDER = 'input[placeholder="Repeat your password"]'
    SIGN_UP_BUTTON = 'button[name="Create Account"]'
    ERROR_MESSAGE = "User already exists"

    def __init__(self, page: Page):
        super().__init__(page)

    def click_create_account(self):
        self.page.get_by_role("button", name="Create one").click()

    def enter_name(self, name: str):
        self.page.get_by_placeholder("John Doe").fill(name)

    def enter_email(self, email: str):
        self.page.get_by_placeholder("you@example.com").fill(email)

    def enter_password(self, password: str):
        self.page.get_by_placeholder("Min. 8 characters").fill(password)

    def enter_confirm_password(self, password: str):
        self.page.get_by_placeholder("Repeat your password").fill(password)

    def click_sign_up(self):
        self.page.get_by_role("button", name="Create Account").click()

    def verify_user_already_exists_error(self) -> bool:
        return self.page.get_by_text(self.ERROR_MESSAGE).is_visible()
