from pytest_bdd import given, when, then, scenarios, parsers
from pages.login_page import LoginPage
from pages.email_page import EmailPage
from playwright.sync_api import Page
import tests.test_login_steps as test_login_steps
from load_env import PASSWORD

scenarios('../features/send_email.feature')

@given(parsers.parse('user is logged in as user "{user}"'))
def login(page: Page, user):
    test_login_steps.open_login_page(page)
    test_login_steps.enter_valid_credentials(page, user)
    test_login_steps.click_login_button(page)
    test_login_steps.verify_email_address_visible(page)
    
@when('the user create new message')
def user_create_new_message(page: Page):
    email_page = EmailPage(page)
    email_page.write_message_click()
    email_page.enter_recipient("iamdory@centrum.sk")
    email_page.enter_subject("test")
    email_page.enter_message("just a test")

def go_to_email_page(page):
    login_page = LoginPage(page)
    login_page.goto_email()


@when('the user clicks the Send button')
def user_clicks_send_button(page: Page):
    email_page = EmailPage(page)	
    email_page.click_send_message()

@then('the user should see that message was sent')
def user_sees_email_sent_message(page: Page):
    pass