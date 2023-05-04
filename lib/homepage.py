from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        self.create_button = (By.XPATH, '//button[contains(text(), "Create Ticket")]')
        self.create_button_modal = (By.CSS_SELECTOR, "div[id='headlessui-dialog-panel-:r1:']")

        # Create Ticket
        self.customer_heading = (By.CSS_SELECTOR, "label[for='customer']")
        self.customer_input = (By.CSS_SELECTOR, "input[id='customer']")
        self.acc_number_heading = (By.CSS_SELECTOR, "label[for='accountNumber']")
        self.acc_number_input = (By.CSS_SELECTOR, "input[id='accountNumber']")
        self.call_id_heading = (By.CSS_SELECTOR, "label[for='callId']")
        self.call_id_input = (By.CSS_SELECTOR, "input[id='callId']")
        self.subject_line_heading = (By.CSS_SELECTOR, "label[for='subject']")
        self.subject_line_input = (By.CSS_SELECTOR, "input[id='subject']")
        self.description_heading = (By.CSS_SELECTOR, "label[for='description']")
        self.description_input = (By.CSS_SELECTOR, "div[id*='ticketDescription']")
        self.queue_heading = (By.CSS_SELECTOR, "label[for='Queue']")
        self.queue_dropdown = (By.XPATH, "//label[@for='Queue']/parent::div/div/child::button")
        self.queue_dropdown_options = (By.XPATH, "//label[@for='Queue']/parent::div/div/ul/li/span")
        self.issue_heading = (By.CSS_SELECTOR, "label[for='issue']")
        self.issue_dropdown = (By.XPATH, "//label[@for='issue']/parent::div/div/child::button")
        self.issue_dropdown_options = (By.XPATH, "//label[@for='issue']/parent::div/div/ul/li/span")
        self.tags_dropdown = (By.CSS_SELECTOR, "label[for='tags'] + div > button")
        self.tags_dropdown_options = (By.CSS_SELECTOR, "label[for='tags'] + div > button +ul > li > span")
        self.tags_heading = (By.CSS_SELECTOR, "label[for='tags']")
        self.customer_type_heading = (By.CSS_SELECTOR, "label[for='customerType']")
        self.customer_type_radio_buttons = (By.CSS_SELECTOR, 'input[id*="customerType"] + label')







