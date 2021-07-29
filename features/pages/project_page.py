"""Project Page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.data.config import settings
from features.driver_factory import driver


class ProjectPage:
    """Page Object class for project page."""
    
    locator_dictionary = {
        "new_project": (By.XPATH, '//span[text()="new project"]'),
        "name": (By.CLASS_NAME, 'input-field-input-wrapper__input'),
        "description": (By.CSS_SELECTOR, '#textarea-field-nameTextArea'),
        "add": (By.XPATH, '//span[text()="Add"]'),
        "validate_project": (By.XPATH, '//span[text()="new project"]'),
    }

    def __init__(self):
        """Init ProjectPage class."""
        self.driver = driver.get_driver()
        self.project_url = settings['project_url']

    def navigate_to_projects(self) -> None:
        """Navigate to project session."""
        self.driver.get(self.project_url)

    def click_on_new_project(self) -> None:
        """Click on new project."""
        element_present = EC.presence_of_element_located((self.locator_dictionary['new_project']))
        WebDriverWait(self.driver, 10).until(element_present)
        self.driver.find_element(*self.locator_dictionary['new_project']).click()

    def enter_project_name(self, name) -> None:
        """Enter project name."""
        self.driver.find_element(*self.locator_dictionary['name']).send_keys(name)

    def enter_project_description(self, description) -> None:
        """Enter project description."""
        self.driver.find_element(*self.locator_dictionary['description']).send_keys(description)

    def add(self) -> None:
        """Add project."""
        self.driver.find_element(*self.locator_dictionary['add']).click()

    def is_project_listed(self, project_name) -> bool:
        """Validate project creation."""
        element_present = EC.presence_of_element_located((By.XPATH, "//span[text()='" + project_name + "']"))
        WebDriverWait(self.driver, 10).until(element_present)

        if self.driver.find_element(By.XPATH, "//span[text()='" + project_name + "']").is_displayed():
            return True
        else:
            return False

    def click_on_existing_project(self,project_name) -> None:
        """Click on pre-created project."""
        element_present = EC.presence_of_element_located((By.XPATH, "//span[text()=" + project_name + "]"))
        WebDriverWait(self.driver, 10).until(element_present)

        self.driver.find_element(By.XPATH, "//span[text()=" + project_name + "]").click()