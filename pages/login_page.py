from .base_page import BasePage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login FORM is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register FORM is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_LINK)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_LINK)
        password_field.send_keys(password)

        password_conf_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONF_LINK)
        password_conf_field.send_keys(password)

        send_btn = self.browser.find_element(*LoginPageLocators.SEND_BTN)
        send_btn.click()
