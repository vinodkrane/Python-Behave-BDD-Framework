"""Steps to test project creation."""
from behave import *
from features.pages.project_page import ProjectPage
from nose.tools import assert_equals, assert_true

project_page = ProjectPage()

@given(u'I visit create project page and click on create project')
def step_impl(context):
    project_page.navigate_to_projects()
    project_page.click_on_new_project()

@when(u'I fill project name with "{project}"')
def step_impl(context, project):
    project_page.enter_project_name(project)

@when(u'I fill project description with "{description}"')
def step_impl(context, description):
    project_page.enter_project_description(description)

@when(u'I press the add')
def step_impl(context):
    project_page.add()


@then(u'"{project}" creation is successful')
def step_impl(context, project):
    assert_true (project_page.is_project_listed(project))
