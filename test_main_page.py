import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
home_link = "http://selenium1py.pythonanywhere.com"
basket_link = 'http://selenium1py.pythonanywhere.com/en-gb/basket/'


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, home_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, home_link)
        page.open()
        page.should_be_login_link()


def test_should_be_login_url(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_form()


def test_should_be_registration_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, home_link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, basket_link, timeout=0)
    page.open()
    page.basket_is_empty()
    page.basket_is_empty_text()
