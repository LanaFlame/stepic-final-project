from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.locators import BasePageLocators
import pytest
import time

#@pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", pytest.param("7",marks=pytest.mark.xfail), "8", "9"])

    #def test_guest_cant_see_success_message(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
        #page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        #page.open()
        #page.test_guest_cant_see_success_message_after_adding_product_to_basket() 

    #def test_guest_can_add_product_to_basket(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
        #page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        #page.open()
        #page.test_guest_cant_see_success_message_before_adding_product_to_basket()                      # открываем страницу
        #page.add_product_to_basket()          # выполняем метод страницы — переходим на страницу
        #page.solve_quiz_and_get_code()
        #page.check_title_and_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.add_product_to_basket()          # выполняем метод страницы — переходим на страницу
    page.solve_quiz_and_get_code()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()

  

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.add_product_to_basket()          # выполняем метод страницы — переходим на страницу
    page.solve_quiz_and_get_code()
    page.test_message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page=BasketPage(browser, browser.current_url)
    basket_page.shouldnt_be_goods()
    basket_page.should_be_message()

@pytest.mark.new
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
        page = LoginPage(browser, link) 
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "734875fdsff344"
        page.register_new_user(email, password)
        page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()
        page.test_guest_cant_see_success_message_after_adding_product_to_basket() 

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()
        page.test_guest_cant_see_success_message_before_adding_product_to_basket()                      # открываем страницу
        page.add_product_to_basket()          # выполняем метод страницы — переходим на страницу
        page.solve_quiz_and_get_code()
        page.check_title_and_price()





