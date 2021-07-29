"""Home Page."""
from features.data.config import settings
from features.driver_factory import driver


class HomePage:
    """Page Object class for home page."""

    def __init__(self):
        """Init HomePage class."""
        self.driver = driver.get_driver()
        self.url = settings['login_url']

    def launch_application(self) -> None:
        """Launch the application."""
        self.driver.get(self.url)

    def close_application(self) -> None:
        """close the application."""
        self.driver.close()