from .pages.login_page import LoginPage
from .pages.main_page import MainPage

main_link = "http://selenium1py.pythonanywhere.com/"
login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, main_link)
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