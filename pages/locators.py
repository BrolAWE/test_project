from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.NAME, "registration-email")
    PASSWORD1_FIELD = (By.NAME, "registration-password1")
    PASSWORD2_FIELD = (By.NAME, "registration-password2")
    BUTTON_FIELD = (By.NAME, "registration_submit")


class ProductPageLocators():
    BASKET_LINK = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_VALUE = (By.TAG_NAME, "strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.LINK_TEXT, "Посмотреть корзину")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_TEXT = (By.LINK_TEXT, "Продолжить покупки")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
