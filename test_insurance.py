import pytest
import json
from pathlib import Path
from playwright.sync_api import Page, expect
from config import BASE_URL
from pages.home_page import HomePage
from pages.package_details_page import PackageDetailsPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.inquiry_form_page import InquiryFormPage

DATA_FILE = Path(__file__).parent / "Data" / "holiday_enquiry.json"
with open(DATA_FILE) as f:
    test_data = json.load(f)
    enquiry_list = test_data['enquiry_data']
    register_list = test_data['register_data']
    login_logout_list = test_data['login_logout_data']
    register_existing_email_list = test_data['register_existing_email_data']
    holiday_enquiry_list = test_data['holiday_enquiry_data']

@pytest.mark.parametrize('enquiry', enquiry_list)
def test_holidays_package_add_to_cart(page : Page, enquiry):
    home = HomePage(page)
    pkg = PackageDetailsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    
    home.navigate_to_home()
    assert home.verify_home_page_visible()
    home.click_menu()
    home.click_search()
    
    home.select_package_by_name(enquiry['package_name'])
    pkg.click_book_package()
    pkg.click_add_to_cart()
    pkg.click_view_cart()
    
    cart.click_checkout()
    
    checkout.enter_sign_in_email(enquiry['sign_in_email'])
    checkout.enter_sign_in_password(enquiry['sign_in_password'])
    checkout.click_sign_in()
    
    cart.click_cart_icon()
    cart_package_name = cart.get_package_name()
    print(cart_package_name)
    assert cart.verify_package_visible()
    assert enquiry['package_name'] in cart_package_name
    
    cart.click_checkout()
    checkout.fill_checkout_form(enquiry['checkout_first_name'],
                                 enquiry['checkout_last_name'], 
                                enquiry['checkout_email'],
                                  enquiry['checkout_mobile'])
    checkout.click_proceed_to_pay()
    


def test_incorrect_login(page : Page):
    login = LoginPage(page)
    home = HomePage(page)
    
    login.goto(BASE_URL)
    home.click_menu()
    login.click_login_button()
    login.enter_email("incorrect@example.com")
    login.enter_password("IncorrectPassword")
    login.click_sign_in()
    expect(page.get_by_text("Invalid credentials")).to_be_visible()


@pytest.mark.parametrize('login_logout', login_logout_list)
def test_login_logout(page : Page, login_logout):
    login = LoginPage(page)
    home = HomePage(page)
    
    login.goto(BASE_URL)
    home.click_menu()
    login.click_login_button()
    login.enter_email(login_logout['email'])
    login.enter_password(login_logout['password'])
    login.click_sign_in()
    
    expect(page.get_by_role("banner").get_by_role("button", name=login_logout['username'])).to_be_visible()
    login.click_user_menu(login_logout['username'])
    login.click_logout()
    expect(page.get_by_role("main").get_by_role("button", name="Login")).to_be_visible()
    

@pytest.mark.parametrize('existing_user', register_existing_email_list)
def test_Register_user_with_existing_email(page : Page, existing_user):
    login = LoginPage(page)
    reg = RegistrationPage(page)
    home = HomePage(page)
    
    login.goto(BASE_URL)
    home.click_menu()
    login.click_login_button()
    reg.click_create_account()
    reg.enter_name(existing_user['register_name'])
    reg.enter_email(existing_user['register_email'])
    reg.enter_password(existing_user['register_password'])
    reg.enter_confirm_password(existing_user['register_password'])
    reg.click_sign_up()
    expect(page.get_by_text(existing_user['error_text'])).to_be_visible()


@pytest.mark.parametrize('holiday_enquiry', holiday_enquiry_list)
def test_Holiday_enquiry(page : Page, holiday_enquiry):
    inquiry = InquiryFormPage(page)
    home = HomePage(page)
    
    home.goto(BASE_URL)
    inquiry.fill_inquiry_form(holiday_enquiry['full_name'], holiday_enquiry['email'], 
                             holiday_enquiry['mobile'], holiday_enquiry['destination'], 
                             holiday_enquiry['date_day'])
    inquiry.click_get_callback()
    inquiry.click_continue_browsing()
    expect(page.get_by_text(holiday_enquiry['success_text'])).to_be_visible()

def test_verify_holiday_package_count(page : Page):
    home = HomePage(page)
    
    home.goto(BASE_URL)
    home.click_menu()
    home.click_search()
    page.wait_for_load_state("networkidle")
    package_count = home.get_package_count()
    print(f"Total holiday packages displayed: {package_count}")
    assert package_count > 0, "No holiday packages are displayed on the homepage."


def test_Delete_product_from_cart_as_a_guestuser(page : Page):
    home = HomePage(page)
    pkg = PackageDetailsPage(page)
    cart = CartPage(page)
    
    home.goto(BASE_URL)
    home.click_menu()
    home.click_search()
    page.wait_for_load_state("networkidle")
    home.click_view_details_first_package()
    pkg.click_book_package()
    pkg.click_add_to_cart()
    pkg.click_view_cart()
    cart.click_remove_item()
    cart.click_remove()
    expect(page.get_by_text("Your cart is empty")).to_be_visible()
    
   
def test_delete_product_from_cart_as_a_loggedin_user(page : Page):
    login = LoginPage(page)
    home = HomePage(page)
    cart = CartPage(page)
    
    home.goto(BASE_URL)
    home.click_menu()
    login.click_login_button()
    login.enter_email("vaibhav@zenithholidays.com")
    login.enter_password("Vaibhav@123")
    login.click_sign_in()
    cart.click_cart_icon()
    cart.click_remove_item()
    cart.click_remove()
    expect(page.get_by_text("Your cart is empty")).to_be_visible()

def test_forget_password_functionality(page : Page):
    page.goto(BASE_URL)
    page.locator(".sr-only").click()
    page.get_by_role("main").get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Forgot password?").click()
    page.get_by_placeholder("you@example.com").fill("vaibhav.sable@zenithholidays.com")
    page.get_by_role("button", name="Send Reset Link").click()
    expect(page.get_by_text("Check your inbox — a reset link has been sent. After resetting, you'll receive a confirmation email.")).to_be_visible()


# def test_request_callback(page : Page):
#     page.goto(BASE_URL)
#     page.locator(".sr-only").click()
#     page.get_by_role("button", name="Search").click()
#     page.wait_for_load_state("networkidle")  # wait for the page to load completely  
#     page.locator("div.flex.flex-col.gap-4 article").nth(0).get_by_role("button", name="View Details").click()
#     page.get_by_role("button", name="Request Callback").click()
#     page.get_by_placeholder("Your Name").fill("Vaibhav Sable")
#     page.get_by_placeholder("Email ID").fill("vaibhav.sable@zenithholidays.com")
#     page.get_by_placeholder("Mobile Number").fill("9876543210")
#     page.get_by_role("textbox", name="Country *").fill("Dubai")
#     page.get_by_role("textbox", name="State *").fill("Dubai")
#     page.get_by_role("textbox", name="City *").fill("Dubai")