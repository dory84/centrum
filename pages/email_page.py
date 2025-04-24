from playwright.sync_api import Page

class EmailPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.landing_page_label = page.inner_text(".product_label")
        self.write_message = page.get_by_role("link", name="Napísať správu")
        self.recipient = page.get_by_role("textbox", name="smart_input_to")	
        self.subject = page.get_by_role("textbox", name="subject")
        self.message = page.get_by_role("textbox", name="message")
        self.send_message = page.locator("#qa_email_send_upper")

    def write_message_click(self):
        self.write_message.click()
        
    def enter_recipient(self, recipient):
        self.recipient.fill(recipient)
        
    def enter_subject(self, subject):
        self.subject.fill(subject)
        
    def enter_message(self, message):
        self.message.fill(message)

        
    def click_send_message(self):
        self.send_message.click()