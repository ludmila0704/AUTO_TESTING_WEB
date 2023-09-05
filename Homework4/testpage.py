import logging
from BaseApp import BasePage
import yaml
from selenium.webdriver.common.by import By


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=5)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    # ENTER TEXT
    def enter_login(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="pass_form")

    def enter_post_title(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_TITLE"], word, description="post_title")

    def enter_post_description(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_DESCRIPTION"], word, description="post_descr")

    def enter_post_content(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_POST_CONTENT"], word, description="post_content")

    def enter_contact_your_name(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_YOUR_NAME"], word,
                                          description="contact_name_field")

    def enter_contact_your_email(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_YOUR_EMAIL"], word,
                                          description="contact_email_field")

    def enter_contact_content(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT"], word,
                                          description="contact_content")

    # click

    def click_login_button(self):
        return self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_create_post_btn(self):
        return self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description="post")

    def click_contact_us_link(self):
        return self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_CONTACT_US"], description="contact us")

    def click_save_btn(self):
        return self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="save")

    def click_save_contact_us_btn(self):
        return self.click_button(TestSearchLocators.ids["LOCATOR_BTN_CONTACT_US"], description="save")

    # GET

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error_text")

    def get_login_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO_LOGIN"], description="login")

    def get_added_post_title(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST_ADDED"], description="post_title")
