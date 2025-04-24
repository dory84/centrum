Feature: User Send Email

Scenario: User successfully send email
    Given user is logged in as user "iamdory84"
    When the user create new message
    And the user clicks the Send button
    Then the user should see that message was sent