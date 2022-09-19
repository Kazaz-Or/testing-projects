import pytest
from WebAppTestingWithPythonSelenium.pages.locators import LocatorsPage


@pytest.mark.usefixtures("pre_test")
class LocatorsTestSuite:

    @pytest.fixture(autouse=True)
    def class_object(self):
        self.locators_page = LocatorsPage(self.driver)

    def test_click_on_locators_page(self):
        self.locators_page.click_on_locators_page()
        self.locators_page.verify_locators_page()

    def test_enter_data_in_edit_box(self):
        self.locators_page.click_on_locators_page()
        self.driver.maximize_window()
        self.locators_page.enter_text()
        self.locators_page.click_on_submit_button()


