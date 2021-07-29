"""Factory class to maintain the instance of browser."""
from selenium import webdriver

class DriverFactory:
    """WebDriver Factory Class."""
    
    instance = None

    def __init__(self):
        """Init DriverFactory class."""
        option = webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(
                executable_path=r'C:/Users/vinod_rane/PycharmProjects/GridSingularityDemo/venv/chromedriver.exe',
                chrome_options=option)

    def get_driver(self):
        """Get the instance of WebDriver."""
        return self.driver

    @classmethod
    def get_instance(cls):
        """Get the instance of DriverFactory."""
        if cls.instance is None:
            cls.instance = DriverFactory()
        return cls.instance

driver = DriverFactory.get_instance()
