import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from lib.homepage import LocatorsHomePage
from utils.read_properties import configs

use_step_matcher("re")


@given('the user is on the "(.*)" portal')
def open_given_portal(context, portal):
    driver = context.browser
    url = portal + "_url"
    driver.get(configs.get("ticketing", url))



@when('the user clicks on the Create Button')
def click_on_create_button(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    error_text = "Create ticket button is not found/clickable"
    time.sleep(3)
    wait.until(EC.visibility_of_element_located(page.create_button), error_text).click()


@then('the create ticket modal is visible')
def verify_ticket_modal(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    try:
        wait.until(EC.visibility_of_element_located(page.create_button_modal))

    except TimeoutException:
        error_text = "Create Ticket modal is not displayed"
        assert False, error_text


@then('the Customer heading and input field are visible')
def verify_customer_input(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    # Verify customer heading
    try:
        wait.until(EC.visibility_of_element_located(page.customer_heading))

    except TimeoutException:
        error_text = "Customer heading is not displayed"
        assert False, error_text

    # Verify customer input field
    try:
        input_field = wait.until(EC.visibility_of_element_located(page.customer_input))
        assert input_field.is_enabled(), "The Customer input field is not enabled"

    except TimeoutException:
        error_text = "Customer input is not displayed"
        assert False, error_text


@then('the Account Number heading and input field are visible')
def verify_acc_number_input(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    # Verify account number heading
    try:
        wait.until(EC.visibility_of_element_located(page.acc_number_heading))

    except TimeoutException:
        error_text = "Account Number heading is not displayed"
        assert False, error_text

    # Verify account input field
    try:
        wait.until(EC.visibility_of_element_located(page.acc_number_input))

    except TimeoutException:
        error_text = "Account Number input is not displayed"
        assert False, error_text


@then('the Call ID heading and input field are visible')
def verify_call_id_input(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    # Verify call id heading
    try:
        wait.until(EC.visibility_of_element_located(page.call_id_heading))

    except TimeoutException:
        error_text = "Call ID heading is not displayed"
        assert False, error_text

    # Verify call id input field
    try:
        wait.until(EC.visibility_of_element_located(page.call_id_input))

    except TimeoutException:
        error_text = "Call ID input is not displayed"
        assert False, error_text


@then('the Subject Line heading and input field are visible')
def verify_subject_line_input(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    # Verify subject line heading
    try:
        wait.until(EC.visibility_of_element_located(page.subject_line_heading))

    except TimeoutException:
        error_text = "Subject Line heading is not displayed"
        assert False, error_text

    # Verify subject line input field
    try:
        wait.until(EC.visibility_of_element_located(page.subject_line_input))

    except TimeoutException:
        error_text = "Subject Line input is not displayed"
        assert False, error_text


@then('the Description heading and input field are visible')
def verify_description_input(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    # Verify Description heading
    try:
        wait.until(EC.visibility_of_element_located(page.description_heading))

    except TimeoutException:
        error_text = "Description heading is not displayed"
        assert False, error_text

    # Verify Description input field
    try:
        wait.until(EC.visibility_of_element_located(page.description_input))

    except TimeoutException:
        error_text = "Description input is not displayed"
        assert False, error_text


@then('the Issue heading is visible with the following dropdown options "(.*)"')
def verify_issue_dropdown(context, given_options):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    # Verify Issues heading
    try:
        wait.until(EC.visibility_of_element_located(page.issue_heading))

    except TimeoutException:
        error_text = "Issues heading is not displayed"
        assert False, error_text

    # Open dropdown
    error_text = "Issues Dropdown not found"
    dropdown = wait.until(EC.element_to_be_clickable(page.issue_dropdown), error_text)
    dropdown.click()

    # Verify dropdown options
    dropdown_options = wait.until(EC.visibility_of_all_elements_located(page.issue_dropdown_options))
    given_options = given_options.split(", ")
    for option in dropdown_options:
        option_value = option.text
        if option_value not in given_options and option_value != "Select Issue...":
            false_message = f"Dropdown option,{option_value}, is not part of given options."
            assert False, false_message

    # Close the dropdown
    dropdown.click()


@then('the Tags heading is visible with the following dropdown options "(.*)"')
def verify_tags_dropdown(context, given_options):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    # Verify Tags heading
    try:
        wait.until(EC.visibility_of_element_located(page.tags_heading))

    except TimeoutException:
        error_text = "Tags heading is not displayed"
        assert False, error_text

    # Open dropdown
    error_text = "Tags Dropdown not found"
    dropdown = wait.until(EC.element_to_be_clickable(page.tags_dropdown), error_text)
    dropdown.click()

    # Verify dropdown options
    dropdown_options = wait.until(EC.visibility_of_all_elements_located(page.tags_dropdown_options))
    given_options = given_options.split(", ")
    for option in dropdown_options:
        option_value = option.text
        if option_value not in given_options:
            false_message = f"Dropdown option,{option_value}, is not part of given options."
            assert False, false_message

    # Close the dropdown
    dropdown.click()


@then('the Queue heading is visible with the following dropdown options "(.*)"')
def verify_queue_dropdown(context, given_options):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    # Verify queue heading
    try:
        wait.until(EC.visibility_of_element_located(page.queue_heading))

    except TimeoutException:
        error_text = "Queue heading is not displayed"
        assert False, error_text

    # Open dropdown
    error_text = "Queue Dropdown not found"
    dropdown = wait.until(EC.element_to_be_clickable(page.queue_dropdown), error_text)
    dropdown.click()

    # Verify dropdown options
    dropdown_options = wait.until(EC.visibility_of_all_elements_located(page.queue_dropdown_options))
    given_options = given_options.split(", ")
    for option in dropdown_options:
        option_value = option.text
        if option_value not in given_options and option_value != "Select Queue...":
            false_message = f"Dropdown option,{option_value}, is not part of given options."
            assert False, false_message

    # Close the dropdown
    dropdown.click()


@then('the Customer Type heading with "(.*)" radio buttons is visible')
def verify_customer_type_radio(context, given_options):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    # Verify Customer Type heading
    try:
        wait.until(EC.visibility_of_element_located(page.customer_heading))

    except TimeoutException:
        error_text = "Customer Type heading is not displayed"
        assert False, error_text

    # Verify Customer type radio buttons
    radio_buttons = wait.until(EC.visibility_of_all_elements_located(page.customer_type_radio_buttons))
    given_options = given_options.split(", ")
    for button in radio_buttons:
        button_value = button.text
        if button_value not in given_options:
            false_message = f"Dropdown option,{button_value}, is not part of given options."
            assert False, false_message
        button.click()




