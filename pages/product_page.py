import math
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Страница продукта"""

    def solve_quiz_and_get_code(self):
        """Решение примера, отображаемого в алерте (для задачи с параметризацией).
        try/except верхнего уровня позволяет использовать код функции
        self.add_to_basket_and_check_name даже на тех страницах, где нет алертов
        и не нужно применять данную функцию"""

        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("No second alert presented")
        except:
            pass

    def should_not_be_success_message(self):
        """Проверяет отсутствие на странице сообщения об успешном добавлении в корзину"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        """Проверяет, что сообщение об успешном добавлении в корзину исчезает"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Didn't notice that success message disappears"

    def add_to_basket(self):
        """Добавляет товар в корзину"""
        self.browser.find_element(*ProductPageLocators.add_to_basket_button).click()

    def book_name_in_catalogue(self):
        """Название книги в каталоге"""
        return self.browser.find_element(*ProductPageLocators.book_name).text

    def book_price_in_catalogue(self):
        """Цена книги в каталоге. Возвращает строку с символом валюты"""
        return self.browser.find_element(*ProductPageLocators.book_price).text

    def book_name_in_basket(self):
        """Название книги, которое отображается в корзине.
        Нужно, чтобы в корзине был только один предмет"""
        return self.browser.find_element(*ProductPageLocators.book_name_in_basket).text

    def book_price_in_basket(self):
        """Цена книги в корзине. Возвращает строку с символом валюты и пробелами.
        Нужно, чтобы в корзине был только один предмет"""
        return self.browser.find_element(*ProductPageLocators.book_price_in_basket).text

    def add_to_basket_and_check_name(self):
        """Сравнивает название книги в каталоге до добавления в корзину
        с названием после добавления"""
        book_name = self.book_name_in_catalogue()
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        book_name2 = self.book_name_in_basket()
        assert book_name2 == book_name, f"Book's name in basket is wrong!\n{self.url}"
