from selenium.common import NoSuchElementException

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def check_basket(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False

    def basket_is_empty(self):
        assert self.check_basket(*BasketPageLocators.BASKET_IS_EMPTY), 'Basket is not empty'

    def basket_is_empty_text(self):
        text = self.browser.find_element(
            *BasketPageLocators.BASKET_IS_EMPTY_TEXT).text
        assert text == 'Your basket is empty. Continue shopping', 'No text "Your basket is empty."'
