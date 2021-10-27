from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty_by_text(self):
        """Проверяет, что на странице корзины есть текст о том, что она пуста"""
        no_items_p = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text.strip()
        no_items_a = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT_LINK).text.strip()
        text_without_link = no_items_p.rstrip(no_items_a).strip()
        assert text_without_link in BasketPageLocators.EMPTY_BASKET_WORDS

    def basket_has_no_items(self):
        """Проверяет, что на странице корзины нет товаров"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL)
