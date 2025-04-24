from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("complementary").locator("input[name=\"userName\"]")
        self.password_input = page.get_by_role("complementary").locator("input[name=\"password\"]")
        self.login_btn = page.get_by_role("button", name="Prihlásiť")
        self.email_label = page.get_by_role("link", name="iamdory84@centrum.sk")
        self.error_message = page.get_by_text("Nesprávne meno alebo heslo")
        self.accept_button = page.get_by_role("button", name="Súhlasím")
        self.logout_button = page.get_by_role("button", name="Odhlásiť")


    def navigate(self):
        self.page.goto("https://www.centrum.sk/")

    def enter_credentials(self, user_name, password):
        self.username_input.fill(user_name)
        self.password_input.fill(password)

    def click_login_btn(self):
        self.login_btn.click()
        
    def click_accept_btn(self):
        self.accept_button.click()
        
    def verify_email_label(self):
        expect(self.email_label).to_be_visible()

    def verify_login_error(self):
        expect(self.error_message).to_be_visible()
        
    def click_logout_btn(self):
        self.logout_button.click()
        
    def verify_username_input(self):
        expect(self.username_input).to_be_visible()
                
    def goto_email(self):
        self.email_label.click()