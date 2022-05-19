import unittest
import pytest

from MobileAndroidTesting.pages.ContactForm import ContactForm


@pytest.mark.usefixtures("pre_run")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object(self):
        self.contact_form = ContactForm(self.driver)

    @pytest.mark.run(order=1)
    def test_open_contact_form(self):
        self.contact_form.click_contact_form_button()
        self.contact_form.verify_contact_page()

    @pytest.mark.run(order=2)
    def test_enter_data_in_from(self):
        self.contact_form.enter_name_field()
        self.contact_form.enter_email_field()
        self.contact_form.enter_email_field()
        self.contact_form.enter_address_field()
        self.contact_form.enter_mobile_number_field()

    @pytest.mark.run(order=3)
    def test_submit_data(self):
        self.contact_form.click_submit_button()
        self.contact_form.filled_page_screenshot()

