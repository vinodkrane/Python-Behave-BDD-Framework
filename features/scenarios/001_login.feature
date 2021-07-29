Feature: Verify Login
"""
Verify if a user will be able to login successfully.
"""
@smoke
Scenario Outline: Verification of Login

Given I visit login page"
When I fill username with "<username>"
  And I fill password with "<password>"
  And I press the login
Then Login is successful

  Examples:
    | username               | password         |
    | vinodkrane@gmail.com   | Na$hirabad       |
