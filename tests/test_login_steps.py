from pytest_bdd import given, when, then, scenarios, parsers
from pages.login_page import LoginPage
from playwright.sync_api import Page
from load_env import PASSWORD

scenarios('../features/login.feature')

# Step definitions
@given("the user is on the login page")
def open_login_page(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()

@when(parsers.parse('the user enters user "{user}" and password "{password}"'))
def enter_credentials(page: Page, user, password):
    login_page = LoginPage(page)
    login_page.click_accept_btn()
    login_page.enter_credentials(user, password)
    
@when(parsers.parse('the user enters user "{user}" and secret password'))
def enter_valid_credentials(page: Page, user):
    login_page = LoginPage(page)
    login_page.click_accept_btn()
    login_page.enter_credentials(user, PASSWORD)


@when('the user clicks the Login button')
def click_login_button(page: Page):
    login_page = LoginPage(page)
    login_page.click_login_btn()

@then('the user should see email address field')
def verify_email_address_visible(page: Page):
    login_page = LoginPage(page)
    login_page.verify_email_label()

@then('the user should see an error message')
def verify_error_message(page: Page):
    print("User can see an error message")
    login_page = LoginPage(page)
    login_page.verify_login_error()
    
@then('the user clicks Logout button')
def click_logout_button(page: Page):
    login_page = LoginPage(page)
    login_page.click_logout_btn()
    
@then('the user should see username field')
def verify_username_field(page: Page):
    login_page = LoginPage(page)
    login_page.verify_username_input()    
    print("User can see username field")
