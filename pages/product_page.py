from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

    def compare_title(self):
        title_on_page = self.browser.find_element(*ProductPageLocators.TITLE).text
        title_on_basket = self.browser.find_element(*ProductPageLocators.BASKET_TITLE).text
        assert title_on_basket == title_on_page, "Book title in order is different to book title in basket"

    def compare_price(self):
        price_on_page = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_on_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert price_on_basket == price_on_page, "Book price in order is different to book price in basket"
