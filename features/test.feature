@smoke
Feature: Create a new Ticket

  Background: Open Create ticket modal on the ticketing portal.
    Given the user is on the "ticketing" portal
    When the user clicks on the Create Button
    Then the create ticket modal is visible

  @TIC_119
  Scenario: Verify the radio buttons, input fields, dropdowns, and headings on the create ticket modal.
    Then the Customer heading and input field are visible
    And the Account Number heading and input field are visible
    And the Call ID heading and input field are visible
    And the Subject Line heading and input field are visible
    And the Description heading and input field are visible
    And the Issue heading is visible with the following dropdown options "Intermittent Connection, Outage, Task"
    And the Tags heading is visible with the following dropdown options "New, Repeat Issue"
    And the Queue heading is visible with the following dropdown options "Customer Support, Billing, Tech Support, Sales"
    And the Customer Type heading with "Enterprise, Commercial, Business, Residential" radio buttons is visible



