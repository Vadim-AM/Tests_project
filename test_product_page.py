import random
import string

import pytest

from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .test_main_page import login_link

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
test_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
basket_link = 'http://selenium1py.pythonanywhere.com/en-gb/basket/'


@pytest.mark.parametrize('num', [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, num):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_title()
    page.compare_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_msg()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, test_link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, test_link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, basket_link, timeout=0)
    page.open()
    page.basket_is_empty()
    page.basket_is_empty_text()


@pytest.mark.test_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        email = ''.join(random.sample(string.ascii_lowercase, 9)) + "@fakemail.com"
        password = ''.join(random.sample(string.digits, 9))
        self.login_page = LoginPage(browser, login_link)
        self.login_page.open()
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()
        return browser

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, test_link, timeout=0)
        page.open()
        page.add_to_basket()
        page.compare_title()
        page.compare_price()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, test_link, timeout=5)
        page.open()
        page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
