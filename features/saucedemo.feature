Feature: SauceDemo Login

    Scenario: Login with valid credentials
        Given I am on the SauceDemo login page
        When I enter with username "standard_user" and password "secret_sauce"
        Then I should be redirected to the inventory page

    @debug
    Scenario: Login with invalid credentials
        Given I am on the SauceDemo login page
        When I enter with username "standard_user" and password "wrong_password"
        Then I should see an error message