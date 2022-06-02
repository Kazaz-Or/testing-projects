import allure

from WebAppTesting.common.base import Base


class LocatorsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _locators_page = "Locators"
    _locators_page_class = "card-body"
    _enter_text_edit_box = "user_input"
    _submit_button = "submitbutton"

    def click_on_locators_page(self):
        self.click_on_element(locator_value=self._locators_page, locator_type="link")

    @allure.step
    def verify_locators_page(self):
        element = self.is_element_displayed(locator_value=self._locators_page_class, locator_type="class")
        assert element == True

    @allure.step
    def enter_text(self):
        self.send_text(text="Kazi 2", locator_value=self._enter_text_edit_box, locator_type="id")

    @allure.step
    def click_on_submit_button(self):
        self.click_on_element(locator_value=self._submit_button, locator_type="id")
