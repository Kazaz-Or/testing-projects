import allure
from allure_commons.types import AttachmentType

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import WebAppTestingWithPythonSelenium.utilities.customLogger as logger


class Base:
    log = logger.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def launch_webpage(self, url, title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info(f"Web page launched with URL: {url}")
        except:
            self.log.info(f"Web page failed to launch with URL: {url}")

    def get_locator_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "tag":
            return By.TAG_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "partiallink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log(f"Locator type {locator_type} not supported")
            return False

    def get_web_element(self, locator_value, locator_type):
        web_element = None
        try:
            locator_type = locator_type.lower()
            locator_by_type = self.get_locator_type(locator_type)
            web_element = self.driver.find_element(locator_by_type, locator_value)
            self.log.info(f"Element found with locator value: {locator_value}, while using locator type: {locator_by_type}")
        except:
            self.log.error(
                f"Element not found with locator value: {locator_value}, while using locator type: {locator_by_type}")
        return web_element

    def wait_for_element(self, locator_value, locator_type):
        web_element = None
        try:
            locator_type = locator_type.lower()
            locator_by_type = self.get_locator_type(locator_type)
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            web_element = wait.until(expected_conditions.presence_of_element_located((locator_by_type, locator_value)))
            self.log.info(
                f"Element found with locator value: {locator_value}, while using locator type: {locator_by_type}")
        except:
            self.log.error(
                f"Element not found with locator value: {locator_value}, while using locator type: {locator_by_type}")
            self.screenshot(locator_type)
        return web_element

    def click_on_element(self, locator_value, locator_type):
        try:
            locator_type = locator_type.lower()
            web_element = self.wait_for_element(locator_value, locator_type)
            web_element.click()
            self.log.info(f"Clicked on element with locator value: {locator_value}, while using locator type: {locator_type}")
        except:
            self.log.error(
                f"Failed to click on element with locator value: {locator_value}, while using locator type: {locator_type}")
            self.screenshot(locator_type)
            assert False

    def send_text(self, locator_value, locator_type, text):
        try:
            locator_type = locator_type.lower()
            web_element = self.wait_for_element(locator_value, locator_type)
            web_element.send_keys(text)
            self.log.info(f"Sent {text} on element with locator value: {locator_value}, while using locator type: {locator_type}")
        except:
            self.log.error(
                f"Failed to send text on element with locator value: {locator_value}, while using locator type: {locator_type}")
            assert False

    def get_text(self, locator_value, locator_type):
        element_text = None
        try:
            locator_type = locator_type.lower()
            web_element = self.wait_for_element(locator_value, locator_type)
            element_text = web_element.text
            self.log.info(f"Got text {element_text}")
        except:
            self.log.error("Failed to get text")

        return element_text

    def is_element_displayed(self, locator_value, locator_type):
        element_displayed = None
        try:
            locator_type = locator_type.lower()
            web_element = self.wait_for_element(locator_value, locator_type)
            element_displayed = web_element.is_displayed()
            self.log.info(f"Element {locator_value}, {locator_type} is displayed")
        except:
            self.log.error("Element is not displayed")

        return element_displayed

    def scroll(self, locator_value, locator_type):
        actions = ActionChains(self.driver)
        try:
            locator_type = locator_type.lower()
            web_element = self.wait_for_element(locator_value, locator_type)
            actions.move_to_element(web_element).perform()
            self.log.info(f"Scrolled to element that has locator value: {locator_value}, with locator type: {locator_type}")
        except:
            self.log.error(
                f"Failed to scroll to element that has locator value: {locator_value}, with locator type: {locator_type}")

    def screenshot(self, filename):
        allure.attach(self.driver.get_screenshot_as_png(), name=filename, attachment_type=AttachmentType.PNG)
