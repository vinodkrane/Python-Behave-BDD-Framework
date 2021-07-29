  Feature: Create a Project
"""
Verify if a user is able to create project.
"""
@smoke
Scenario Outline: Verification of Project Creation

Given I visit create project page and click on create project
When I fill project name with "<project_name>"
  And I fill project description with "<project_description>"
  And I press the add
Then "<project_name>" creation is successful

  Examples:
    | project_name               | project_description         |
    | Reports                    | This is example project     |
