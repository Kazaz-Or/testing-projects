from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import MobileAndroidTesting.utilities.CustomLogger as log

log = log.custom_logger()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_value, locator_type):
        locator_type = locator_type.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locator_type == "id":
            element = wait.until(lambda x: x.find_element(By.ID, locator_value))
            log.info(f"Locator value: {locator_value}, locator type: {locator_type}")
            return element
        elif locator_type == "class":
            element = wait.until(lambda x: x.find_element(By.CLASS_NAME, locator_value))
            log.info(f"Locator value: {locator_value}, locator type: {locator_type}")
            return element
        elif locator_type == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('new UiSelector().description("%s")' % (locator_value)))
            log.info(f"Locator value: {locator_value}, locator type: {locator_type}")
            return element
        elif locator_type == "index":
            element = wait.until(
                lambda x: x.find_element(By.ANDROID_UIAUTOMATOR, 'UiSelector().index(%d)' % int(locator_value)))
            log.info(f"Locator value: {locator_value}, locator type: {locator_type}")
            return element
        elif locator_type == "text":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('new UiSelector().text("%s")' % locator_value))
            log.info(f"Locator value: {locator_value}, locator type: {locator_type}")
            return element
        elif locator_type == "xpath":
            element = wait.until(lambda x: x.find_element(By.XPATH, '%s' % locator_value))
            log.info(f"Locator value: {locator_value}, locator type: {locator_type}")
            return element
        else:
            log.error(f"Locator value {locator_value} not found")
            return element

    def click_element(self, locator_value, locator_type):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.click()
            log.info(f"Clicked on element {locator_value}")
        except:
            log.error(f"Element {locator_value} is not clickable")
        return element

    def send_text(self, locator_value, locator_type, text):
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.send_keys(text)
            log.info(f"Wrote {text} to element {locator_value}")
        except:
            log.error(f"Failed to write {text} into element {locator_value}")

    def is_displayed(self, locator_value, locator_type):
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.is_displayed()
            log.info(f"Element {locator_value} is displayed")
            return True
        except:
            log.error(f"Element {locator_value} is not displayed")
            return False
