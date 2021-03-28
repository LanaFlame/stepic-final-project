from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
	EMPTY_BASKET = (By.CSS_SELECTOR, "#basket_formset")
	EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
class ProductPageLocators():
	ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

	BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
	BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")

	BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) .alertinner p strong")

	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
