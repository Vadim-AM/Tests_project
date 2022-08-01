from .pages.product_page import ProductPage

product_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear)'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_title()
    page.compare_price()
