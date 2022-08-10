from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REG_EMAIL_FORM = (By.ID, 'id_registration-email')
    REG_PASSWORD_FORM = (By.ID, 'id_registration-password1')
    SUBMIT_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    TITLE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    BASKET_TITLE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    BASKET_PRICE = (
        By.CSS_SELECTOR,
        '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form > button')


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (
        By.PARTIAL_LINK_TEXT, 'basket')


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#basket_formset')
    BASKET_IS_EMPTY_TEXT = (By.ID, 'content_inner')
