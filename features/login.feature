Feature: User Login

Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters user "iamdory84" and secret password
    And the user clicks the Login button
    Then the user should see email address field
    And the user clicks Logout button
    Then the user should see username field

Scenario: Login with invalid credentials
    Given the user is on the login page
    When the user enters user "Invalid" and password "invalid_password"
    And the user clicks the Login button
    Then the user should see an error message
