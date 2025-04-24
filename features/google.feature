Feature: Google Home Page

  Scenario: Verify Google homepage title
    Given I open the Google homepage
    Then the title should be "Google"
