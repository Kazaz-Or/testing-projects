import time
import pytest

from MobileAndroidTesting.base.DriverClass import Driver


@pytest.fixture(scope='class')
def pre_run(request):
    driver1 = Driver()
    driver = driver1.get_driver_method()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(4)
    driver.quit()
