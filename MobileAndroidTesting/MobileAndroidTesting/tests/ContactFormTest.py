import time

from MobileAndroidTesting.base.DriverClass import Driver
import MobileAndroidTesting.utilities.CustomLogger as log
from MobileAndroidTesting.base.BasePage import BasePage

driver1 = Driver()
log = log.custom_logger()

driver = driver1.get_driver_method()

base_page = BasePage(driver)
log.info("Launching Application")

base_page.is_displayed("com.code2lead.kwad:id/ContactUs", "id")
base_page.click_element("com.code2lead.kwad:id/ContactUs", "id")
base_page.screenshot("ContactUsPage")

base_page.is_displayed("com.code2lead.kwad:id/Et2", "id")
base_page.send_text("com.code2lead.kwad:id/Et2", "id", "Name")
base_page.is_displayed("com.code2lead.kwad:id/Et3", "id")
base_page.send_text("com.code2lead.kwad:id/Et3", "id", "myemail@blabla.com")
base_page.is_displayed("com.code2lead.kwad:id/Et6", "id")
base_page.send_text("com.code2lead.kwad:id/Et6", "id", "Givatayim Rocks, IL")
base_page.is_displayed("com.code2lead.kwad:id/Et7", "id")
base_page.send_text("com.code2lead.kwad:id/Et7", "id", "050-555587")
base_page.is_displayed("com.code2lead.kwad:id/Btn2", "id")
base_page.screenshot("ContactUsPage_WithText")

base_page.click_element("com.code2lead.kwad:id/Btn2", "id")
base_page.screenshot("ContactUs_AfterSubmit")

time.sleep(4)
driver.quit()
