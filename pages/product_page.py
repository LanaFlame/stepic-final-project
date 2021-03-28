from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasePageLocators
import time
import pytest

class ProductPage(BasePage): 

	def test_guest_cant_see_success_message_before_adding_product_to_basket(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
		"Successed message is presented before adding product to basket, but should not be"

	def add_product_to_basket(self):
		add_product_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
		add_product_button.click()

	def check_title_and_price(self):
		book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
		book_name = book_name.text
		book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET)
		book_name_in_basket = book_name_in_basket.text

		assert book_name==book_name_in_basket, 'Titles do not match'

		book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
		book_price = book_price.text
		book_price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET)
		book_price_in_basket = book_price_in_basket.text

		assert book_price==book_price_in_basket, 'Prices do not match'

	def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
       "Successed message is presented, but should not be"

	def test_message_disappeared_after_adding_product_to_basket(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
       "Successed message does not desappeared, but should be"

