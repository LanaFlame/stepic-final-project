from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage): 
    #def go_to_product_page(self):
        #product_link = self.browser.find_element(*MainPageLocators.PRODUCT_LINK)
        #product_link.click()
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

