"""Login Page."""
from features.driver_factory import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object class for login page."""

    locator_dictionary = {
        "email": (By.CSS_SELECTOR, 'input#email.textInput__input'),
        "password": (By.CSS_SELECTOR, 'input#password.textInput__input'),
        "login_button": (By.CLASS_NAME, 'button__label'),
        "home": (By.XPATH, '//h1[contains(text(), "Home")]')
    }

    def __init__(self):
        """Init LoginPage class."""
        self.driver = driver.get_driver()

    def enter_username(self, email_id) -> None:
        """Enter username."""
        self.driver.find_element(*self.locator_dictionary['email']).send_keys(email_id)

    def enter_password(self, password) -> None:
        """Enter password."""
        self.driver.find_element(*self.locator_dictionary['password']).send_keys(password)

    def submit(self) -> None:
        """submit."""
        self.driver.find_element(*self.locator_dictionary['login_button']).click()

    def validate_login(self) -> bool:
        """Validate login."""
        element_present = EC.presence_of_element_located((self.locator_dictionary['home']))
        WebDriverWait(self.driver, 10).until(element_present)

        text = self.driver.find_element(*self.locator_dictionary['home']).text
        if text == "Home":  return True
        else:   return False
