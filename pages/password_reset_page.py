from playwright.sync_api import Page
from pages.base_page import BasePage


class PasswordResetPage(BasePage):
    FORGOT_PASSWORD_BUTTON = 'button[name="Forgot password?"]'
    EMAIL_PLACEHOLDER = 'input[placeholder="you@example.com"]'
    SEND_RESET_LINK_BUTTON = 'button[name="Send Reset Link"]'
    SUCCESS_MESSAGE = "Check your inbox — a reset link has been sent. After resetting, you'll receive a confirmation email."

    def __init__(self, page: Page):
        super().__init__(page)

    def click_forgot_password(self):
        self.page.get_by_role("button", name="Forgot password?").click()

    def enter_email(self, email: str):
        self.page.get_by_placeholder("you@example.com").fill(email)

    def click_send_reset_link(self):
        self.page.get_by_role("button", name="Send Reset Link").click()

    def verify_reset_link_sent_message(self) -> bool:
        return self.page.get_by_text(self.SUCCESS_MESSAGE).is_visible()
