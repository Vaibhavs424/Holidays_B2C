from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_BUTTON_MAIN = 'button[name="Login"]'
    EMAIL_PLACEHOLDER = 'input[placeholder="you@example.com"]'
    PASSWORD_PLACEHOLDER = 'input[placeholder="Min. 8 characters"]'
    SIGN_IN_BUTTON = 'button[name="Sign In"]'
    FORGOT_PASSWORD_BUTTON = 'button[name="Forgot password?"]'
    ERROR_MESSAGE = "Invalid credentials"

    def __init__(self, page: Page):
        super().__init__(page)

    def click_login_button(self):
        self.page.wait_for_selector('button[name="Login"]', timeout=15000)
        self.page.get_by_role("main").get_by_role("button", name="Login").click()

    def enter_email(self, email: str):
        self.page.get_by_placeholder("you@example.com").fill(email)

    def enter_password(self, password: str):
        self.page.get_by_placeholder("Min. 8 characters").fill(password)

    def click_sign_in(self):
        self.page.get_by_role("button", name="Sign In").nth(1).click()

    def verify_invalid_credentials_error(self) -> bool:
        return self.page.get_by_text(self.ERROR_MESSAGE).is_visible()

    def click_forgot_password(self):
        self.page.get_by_role("button", name="Forgot password?").click()

    def verify_login_button_visible(self) -> bool:
        return self.page.get_by_role("main").get_by_role("button", name="Login").is_visible()

    def verify_user_button_visible(self, username: str) -> bool:
        return self.page.get_by_role("banner").get_by_role("button", name=username).is_visible()

    def click_user_menu(self, username: str):
        self.page.get_by_role("main").get_by_role("button", name=username).click()

    def click_logout(self):
        self.page.locator(".text-red-600").click()
