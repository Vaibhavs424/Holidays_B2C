from playwright.sync_api import Page
from conftest import page
from pages.base_page import BasePage

def __init__(self, page: Page):
        super().__init__(page)

def Select_payment_method(self, method: str):
        self.page.get_by_locator("l1Item__content").nth(2).click()

def Select_Bank(self, bank: str):
        self.page.get_by_name("Test bank").click()

def Continue_to_Pay(self):
        self.page.get_by_role("button", name="PROCEED").click()

def Enter_user_id(self):
        self.page.get_by_placeholder("Enter payu as username").fill("payu")

def Enter_password(self):
        self.page.get_by_placeholder("Enter payu as password").fill("payu")

def Click_submit(self):
        self.page.get_by_locator(".cmn-btn").click()

def select_successful_payment(self):
        self.page.get_by_text("Simulate Success Response").click()