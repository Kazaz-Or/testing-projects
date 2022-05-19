from MobileAndroidTesting.base.BasePage import BasePage


class ContactForm(BasePage):
    def __init__(self, driver):
        super(ContactForm, self).__init__(driver)
        self.driver = driver

    _contact_form = "com.code2lead.kwad:id/ContactUs"
    _page_title = "Contact Us form"  # text type
    _field_enter_name = "com.code2lead.kwad:id/Et2"
    _field_email = "com.code2lead.kwad:id/Et3"
    _field_address = "com.code2lead.kwad:id/Et6"
    _field_mobile_number = "com.code2lead.kwad:id/Et7"
    _submit_button = "com.code2lead.kwad:id/Btn2"

    def click_contact_form_button(self):
        self.click_element(self._contact_form, "id")

    def verify_contact_page(self):
        element = self.is_displayed(self._page_title, "text")
        assert element == True
        self.screenshot("contact_page_form")

    def enter_name_field(self):
        self.send_text(locator_value=self._field_enter_name, locator_type="id", text="Name")

    def enter_email_field(self):
        self.send_text(locator_value=self._field_email, locator_type="id", text="kazi@blabla.com")

    def enter_address_field(self):
        self.send_text(locator_value=self._field_address, locator_type="id", text="Givatayim Rocks, IL")

    def enter_mobile_number_field(self):
        self.send_text(locator_value=self._field_mobile_number, locator_type="id", text="055-066-7777")

    def click_submit_button(self):
        self.click_element(locator_value=self._submit_button, locator_type="id")

    def filled_page_screenshot(self):
        self.screenshot("contactformpage_with_fields")


