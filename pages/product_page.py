from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

    def should_not_be_success_msg(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
