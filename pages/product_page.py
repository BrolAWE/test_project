import pytest
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def __init__(self, browser, url, correct_name, correct_price):
        super().__init__(browser, url)
        self.correct_name = correct_name
        self.correct_price = correct_price

    def add_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        button.click()

    def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_in_url("catalogue"), "Неправильная страница"

    def should_be_button(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*ProductPageLocators.BASKET_LINK), "Нет кнопки добавления"

    def check_name(self):
        # реализуйте проверку, что есть форма логина
        real_name = self.browser.find_elements(By.CLASS_NAME, "alertinner ")[0].find_element(*ProductPageLocators.NAME_VALUE).text
        assert (real_name == self.correct_name), "Название товара не совпадает"

    def check_price(self):
        # реализуйте проверку, что есть форма логина
        real_price = self.browser.find_elements(By.CLASS_NAME, "alertinner ")[2].find_element(*ProductPageLocators.NAME_VALUE).text
        assert (real_price == self.correct_price), "Цена товара не совпадает"

    @pytest.mark.xfail
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе есть, но его быть не должно"

    def should_not_be_success_message_1(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение обу успехе есть"

    @pytest.mark.xfail
    def should_not_be_success_message_2(self):
        assert not self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе есть"
