import time
import pytest

from WebAppTesting.common.base import Base
from WebAppTesting.common.webdriver import WebDriver


@pytest.fixture(scope='class')
def pre_test(request):
    driver_init = WebDriver()
    driver = driver_init.get_webdriver("chrome")
    base_page = Base(driver)
    base_page.launch_webpage("http://dummypoint.com/seleniumtemplate.html", "Selenium Template - Dummy Point")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(3)
    driver.quit()
