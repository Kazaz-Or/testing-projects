from selenium import webdriver
import WebAppTesting.utilities.customLogger as logger


class WebDriver:
    log = logger.custom_logger()

    def get_webdriver(self, browser):
        driver = None
        if browser == "chrome":
            driver = webdriver.Chrome(executable_path="/Users/kazi/Downloads/chromedriver")
            self.log.info(f"Launched {browser} browser")
        elif browser == "safari":
            driver = webdriver.Safari()
            self.log.info(f"Launched {browser} browser")
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path="/Users/kazi/Downloads/geckodriver")
            self.log.info(f"Launched {browser} browser")
        elif browser == "edge":
            driver = webdriver.Edge(executable_path="/Users/kazi/Downloads/edgedriver_mac64")
            self.log.info(f"Launched {browser} browser")

        return driver
