Feature: Create a simulation
"""
Verify if a user is able to create project.
"""
@smoke
Scenario Outline: Verification of Project Creation

Given I select "<project_name>" and create simulation
When I click on next
Then simulation creation is successful under project <project_name>

  Examples:
    | project_name               | simulation                  |
    | Reports                    | R1Simulation                |
