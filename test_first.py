# from playwright.sync_api import Playwright,Page
# import pytest
# import json
# from pathlib import Path
# from playwright.sync_api import expect
# from config import BASE_URL


# DATA_FILE = Path(__file__).parent / "Data" / "holiday_enquiry.json"
# with open(DATA_FILE) as f:
#     test_data = json.load(f)
#     enquiry_list = test_data['enquiry_data']
#     register_list = test_data['register_data']
#     login_logout_list = test_data['login_logout_data']
#     register_existing_email_list = test_data['register_existing_email_data']
#     holiday_enquiry_list = test_data['holiday_enquiry_data']

# @pytest.mark.parametrize('enquiry', enquiry_list)
# def test_holidays_package_add_to_cart(page : Page, enquiry):

#     page.goto("https://zenith-main.zenithholidays.com/")

#     assert page.locator(".bg-background").is_visible()

#     page.locator(".sr-only").click()

#     page.get_by_role("button", name="Search").click()
  
#     package_name = enquiry['package_name']
#     page.locator("div.flex.flex-col.gap-4 article").filter(has_text=package_name).get_by_role("button", name="View Details").click()

#     page.locator("div.flex.flex-col.gap-4 article").count()

#     page.get_by_role("button", name="Book This Package").click()

#     page.get_by_role("button", name="Add to Cart").click()

#     page.get_by_role("button", name="View Cart").click()

#     page.get_by_role("button", name="Checkout").click()

#     page.get_by_placeholder("you@example.com").fill(enquiry['sign_in_email'])

#     page.get_by_placeholder("Min. 8 characters").fill(enquiry['sign_in_password'])


#     page.pause()

#     page.locator(".lucide-shopping-cart").click()

#     cart_package_name = page.locator(".leading-snug").text_content()

#     print(cart_package_name)

#     assert page.locator(".leading-snug").is_visible()

#     assert package_name in cart_package_name

#     page.get_by_role("button", name="Checkout").click()

#     page.get_by_role("textbox", name="First name").fill(enquiry['checkout_first_name'])

#     page.get_by_role("textbox", name="Last name").fill(enquiry['checkout_last_name'])

#     page.get_by_role("textbox", name="email").fill(enquiry['checkout_email'])

#     page.get_by_role("textbox", name="Mobile").fill(enquiry['checkout_mobile'])

#     page.get_by_role("button", name="Proceed to Pay").click()
    


# # @pytest.mark.parametrize('register', register_list)
# # def test_register(page : Page, register):
# #     page.goto("https://zenith-main.zenithholidays.com/")
# #     page.locator(".sr-only").click()
# #     page.get_by_role("button", name="Login").click()
# #     page.get_by_role("button", name="Create one").click()
# #     page.get_by_placeholder("John Doe").fill(register['register_name'])
# #     page.get_by_placeholder("you@example.com").fill(register['register_email'])
# #     page.get_by_placeholder("Min. 8 characters").fill(register['register_password'])
# #     page.get_by_placeholder("Repeat your password").fill(register['register_password'])
# #     page.get_by_role("button", name="Create Account").click()
# #     assert page.url == register['expected_url']

    

# def test_incorrect_login(page : Page):
#     page.goto(BASE_URL)
#     page.locator(".sr-only").click()
#     page.get_by_role("main").get_by_role("button", name="Login").click()
#     page.get_by_placeholder("you@example.com").fill("incorrect@example.com")
#     page.get_by_placeholder("Min. 8 characters").fill("IncorrectPassword")
#     page.get_by_role("button", name="Sign In").nth(1).click()
#     expect (page.get_by_text("Invalid credentials")).to_be_visible()


# @pytest.mark.parametrize('login_logout', login_logout_list)
# def test_login_logout(page : Page, login_logout):
#     page.goto(BASE_URL)
#     page.locator(".sr-only").click()
#     page.get_by_role("main").get_by_role("button", name="Login").click()
#     page.get_by_placeholder("you@example.com").fill(login_logout['email'])
#     page.get_by_placeholder("Min. 8 characters").fill(login_logout['password'])
#     page.get_by_role("button", name="Sign In").nth(1).click()
#     # page.locator("lucide-chevron-down").nth(0).click()
#     expect(page.get_by_role("banner").get_by_role("button", name=login_logout['username'])).to_be_visible()
#     page.get_by_role("main").get_by_role("button", name=login_logout['username']).click()
#     page.locator(".text-red-600").click()
#     expect(page.get_by_role("main").get_by_role("button", name="Login")).to_be_visible()

    

# @pytest.mark.parametrize('existing_user', register_existing_email_list)
# def test_Register_user_with_existing_email(page : Page, existing_user):
#     page.goto(BASE_URL)
#     page.locator(".sr-only").click()
#     page.get_by_role("main").get_by_role("button", name="Login").click()
#     page.get_by_role("button", name="Create one").click()
#     page.get_by_placeholder("John Doe").fill(existing_user['register_name'])
#     page.get_by_placeholder("you@example.com").fill(existing_user['register_email'])
#     page.get_by_placeholder("Min. 8 characters").fill(existing_user['register_password'])
#     page.get_by_placeholder("Repeat your password").fill(existing_user['register_password'])
#     page.get_by_role("button", name="Create Account").click()
#     expect(page.get_by_text(existing_user['error_text'])).to_be_visible()



# @pytest.mark.parametrize('holiday_enquiry', holiday_enquiry_list)
# def test_Holiday_enquiry(page : Page, holiday_enquiry):
#     page.goto(BASE_URL)
#     page.get_by_placeholder("Enter your full name").fill(holiday_enquiry['full_name'])

#     page.get_by_placeholder("you@example.com").fill(holiday_enquiry['email'])

#     page.get_by_placeholder("10-digit mobile number").fill(holiday_enquiry['mobile'])

#     page.get_by_placeholder("e.g. Bali, Dubai, Kashmir").fill(holiday_enquiry['destination'])

#     page.get_by_role("button", name="Select travel date").click()

#     page.locator("tbody tr td").nth(holiday_enquiry['date_day']).click()

#     page.get_by_role("button", name="Get Free Callback").click()

#     page.get_by_role("button", name="Continue Browsing").click()

#     expect(page.get_by_text(holiday_enquiry['success_text'])).to_be_visible()



# def test_verify_holiday_package_count(page : Page):
#     page.goto(BASE_URL)
#     page.locator(".sr-only").click()
#     page.get_by_role("button", name="Search").click()
#     page.wait_for_load_state("networkidle")  # wait for the page to load completely  
#     package_count = page.locator("div.flex.flex-col.gap-4 article").count()
#     print(f"Total holiday packages displayed: {package_count}")
#     assert package_count > 0, "No holiday packages are displayed on the homepage."


# def test_Delete_product_from_cart_as_a_guestuser(page : Page):
#     page.goto(BASE_URL)
#     page.locator(".sr-only").click()
#     page.get_by_role("button", name="Search").click()
#     page.wait_for_load_state("networkidle")  # wait for the page to load completely  
#     page.locator("div.flex.flex-col.gap-4 article").nth(0).get_by_role("button", name="View Details").click()
#     page.get_by_role("button", name="Book This Package").click()
#     page.get_by_role("button", name="Add to Cart").click()
#     page.get_by_role("button", name="View Cart").click()
#     page.locator(".transition-shadow")
#     page.get_by_role("button", name="Remove item").click()
#     page.get_by_role("button", name="Remove").click()
#     expect(page.get_by_text("Your cart is empty")).to_be_visible()
    
   
    
# def test_delete_product_from_cart_as_a_loggedin_user(page : Page):
#     page.goto(BASE_URL)
#     page.locator(".sr-only").click()
#     page.get_by_role("main").get_by_role("button", name="Login").click()
#     page.get_by_placeholder("you@example.com").fill("vaibhav@zenithholidays.com")
#     page.get_by_placeholder("Min. 8 characters").fill("Vaibhav@123")
#     page.get_by_role("button", name="Sign In").nth(1).click()
#     page.locator(".lucide-shopping-cart").click()
#     page.get_by_role("button", name="Remove item").click()
#     page.get_by_role("button", name="Remove").click()
#     expect(page.get_by_text("Your cart is empty")).to_be_visible()


# @pytest.mark.smoke
# def test_search_holiday_package_throught_filter_searchbar(page : Page):
#     page.goto(BASE_URL)
#     page.locator(".sr-only").click()
#     page.get_by_role("button", name="Search").click()
#     page.wait_for_load_state("networkidle")  # wait for the page to load completely  
#     page.get_by_placeholder("Type package name…").fill("Rajasthan Heritage Safari")
#     page.wait_for_load_state("networkidle")  # wait for the search results to load completely 
#     # expect(page.locator("div.flex.flex-col.gap-4 article")).to_have_text("Rajasthan Heritage Safariii")
#     assert "Rajasthan Heritage Safariii" in page.locator("div.flex.flex-col.gap-4 article").all_text_contents()


# def test_forget_password_functionality(page : Page):
#     page.goto(BASE_URL)
#     page.locator(".sr-only").click()
#     page.get_by_role("main").get_by_role("button", name="Login").click()
#     page.get_by_role("button", name="Forgot password?").click()
#     page.get_by_placeholder("you@example.com").fill("vaibhav.sable@zenithholidays.com")
#     page.get_by_role("button", name="Send Reset Link").click()
#     expect(page.get_by_text("Check your inbox — a reset link has been sent. After resetting, you'll receive a confirmation email.")).to_be_visible()


# # def test_request_callback(page : Page):
# #     page.goto(BASE_URL)
# #     page.locator(".sr-only").click()
# #     page.get_by_role("button", name="Search").click()
# #     page.wait_for_load_state("networkidle")  # wait for the page to load completely  
# #     page.locator("div.flex.flex-col.gap-4 article").nth(0).get_by_role("button", name="View Details").click()
# #     page.get_by_role("button", name="Request Callback").click()
# #     page.get_by_placeholder("Your Name").fill("Vaibhav Sable")
# #     page.get_by_placeholder("Email ID").fill("vaibhav.sable@zenithholidays.com")
# #     page.get_by_placeholder("Mobile Number").fill("9876543210")
# #     page.get_by_role("textbox", name="Country *").fill("Dubai")
# #     page.get_by_role("textbox", name="State *").fill("Dubai")
# #     page.get_by_role("textbox", name="City *").fill("Dubai")