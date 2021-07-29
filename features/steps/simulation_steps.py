"""Steps to test simulation creation."""
from behave import *
from nose.tools import assert_equals, assert_true
from features.pages.project_page import ProjectPage
from features.pages.simulation_page import SimulationPage

project_page = ProjectPage()
simulation_page = SimulationPage()

@given(u'I select {project1} and create simulation')
def step_impl(context, project1):
    project_page.navigate_to_projects()
    project_page.click_on_existing_project(project1)
    simulation_page.new_simulation()

@when(u'I click on next')
def step_impl(context):
    simulation_page.click_on_next()


@then(u'simulation creation is successful under project {project1}')
def step_impl(context, project1):
    project_page.navigate_to_projects()
    assert_true(simulation_page.is_simulation_listed(project1))
