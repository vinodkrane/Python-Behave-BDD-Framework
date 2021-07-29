"""Steps to test login."""
from behave import *
from nose.tools import assert_equals, assert_true
from features.pages.home_page import HomePage
from features.pages.login_page import LoginPage

homepage = HomePage()
login_page = LoginPage()

@given(u'I visit login page"')
def step_impl(context):
    homepage.launch_application()

@when(u'I fill username with "{email}"')
def step_impl(context,email):
    login_page.enter_username(email)

@when(u'I fill password with "{password}"')
def step_impl(context,password):
    login_page.enter_password(password)

@when(u'I press the login')
def step_impl(context):
    login_page.submit()

@then(u'Login is successful')
def step_impl(context):
    assert_true (login_page.validate_login())