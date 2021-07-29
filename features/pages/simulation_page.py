"""Simulation Page."""
from selenium.webdriver.common.by import By
from features.driver_factory import driver
from features.data.config import settings
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SimulationPage:
    """Page Object class for Simulation page."""

    locator_dictionary = {
        "new_simulation": (By.XPATH, '//span[text()="new simulation"]'),
        "simulation_name": (By.XPATH, '//*[@id="input-field-name"]'),
        "next": (By.XPATH, '//span[text()="Next"]')
    }

    def __init__(self):
        """Init SimulationPage class."""
        self.driver = driver.get_driver()
        self.project_url = settings['project_url']

    def new_simulation(self) -> None:
        """Create new simulation."""
        self.driver.find_element(*self.locator_dictionary['new_simulation']).click()

    def enter_simulation_name(self, simulation_name) -> None:
        """Enter simulation name."""
        self.driver.find_element(*self.locator_dictionary['simulation_name']).clear()
        self.driver.find_element(*self.locator_dictionary['simulation_name']).send_keys(simulation_name)

    def click_on_next(self) -> None:
        """Click on next."""
        element_present = EC.presence_of_element_located((self.locator_dictionary['next']))
        WebDriverWait(self.driver, 10).until(element_present)

        self.driver.find_element(*self.locator_dictionary['next']).click()

    def is_simulation_listed(self, project_name) -> None:
        """Validate simulation."""
        self.driver.find_element(By.XPATH, "//span[text()='" + project_name + "']").click()

        element_present = EC.presence_of_element_located((By.XPATH, "//p[text()=\"default simulation\"]"))
        WebDriverWait(self.driver, 10).until(element_present)

        if self.driver.find_element(By.XPATH, "//p[text()=\"default simulation\"]").is_displayed():
            return True
        else:
            return False