import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import time


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductPage(browser, link, "Coders at Work", "19,99 £")
    page.open()
    page.add_basket()
    page.solve_quiz_and_get_code()
    page.check_name()
    page.check_price()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link, "Coders at Work", "19,99 £")
    page.open()  # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, "Coders at Work", "19,99 £")
    page.open()
    page.add_basket()
    # page.solve_quiz_and_get_code()
    page.check_name()
    page.check_price()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, "Coders at Work", "19,99 £")
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, "Coders at Work", "19,99 £")
    page.open()
    page.add_basket()
    # page.solve_quiz_and_get_code()
    page.check_name()
    page.check_price()
    time.sleep(1)
    page.should_not_be_success_message_2()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, "Coders at Work", "19,99 £")
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_empty_text()


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link, "Coders at Work", "19,99 £")
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
        page = ProductPage(browser, link, "Coders at Work", "19,99 £")
        page.open()
        page.add_basket()
        page.solve_quiz_and_get_code()
        page.check_name()
        page.check_price()
