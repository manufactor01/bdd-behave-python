Feature: DuckDuckGo Search

  Scenario: User searches for a term
    Given I am on the DuckDuckGo homepage
    When I search for the configured term
    Then I should see results related to the search term
