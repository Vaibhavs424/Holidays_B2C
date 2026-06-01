from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ICON = ".lucide-shopping-cart"
    PACKAGE_NAME_LOCATOR = ".leading-snug"
    REMOVE_ITEM_BUTTON = 'button[name="Remove item"]'
    REMOVE_BUTTON = 'button[name="Remove"]'
    EMPTY_CART_MESSAGE = "Your cart is empty"
    CHECKOUT_BUTTON = 'button[name="Checkout"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def click_cart_icon(self):
        self.page.locator(self.CART_ICON).click()

    def get_package_name(self) -> str:
        return self.page.locator(self.PACKAGE_NAME_LOCATOR).text_content()

    def verify_package_visible(self) -> bool:
        return self.page.locator(self.PACKAGE_NAME_LOCATOR).is_visible()

    def click_remove_item(self):
        self.page.get_by_role("button", name="Remove item").click()

    def click_remove(self):
        self.page.get_by_role("button", name="Remove").click()

    def verify_cart_empty(self) -> bool:
        return self.page.get_by_text(self.EMPTY_CART_MESSAGE).is_visible()

    def click_checkout(self):
        self.page.get_by_role("button", name="Checkout").click()
