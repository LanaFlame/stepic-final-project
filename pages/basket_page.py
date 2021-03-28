from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
import time
import pytest

class BasketPage(BasePage):
	def shouldnt_be_goods(self):
		assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET),\
		"Goods is presented, but should not be"
	def should_be_message(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE),\
		"Message 'Your basket is empty' is not presented"