import pytest

from WebAppTestingWithPythonSelenium.common.base import Base
from WebAppTestingWithPythonSelenium.pages.form import FormPage


@pytest.mark.usefixtures("pre_test")
class FormPageTestSuite:

    @pytest.fixture(autouse=True)
    def class_object(self):
        self.form_page = FormPage(self.driver)
        self.base_page = Base(self.driver)

    def test_form_page(self):
        self.form_page.click_form()
        self.form_page.verify_form_page()

    def test_enter_data_on_form_page(self):
        self.form_page.click_form()
        self.form_page.enter_name()
        self.form_page.enter_email()
        self.form_page.click_radio_button()
        self.form_page.enter_technology()
        self.form_page.enter_message()
        self.form_page.enter_captcha()
        self.form_page.click_on_post_button()
