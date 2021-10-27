import math
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators

class ProductPage(BasePage):
    """Страница продукта"""

    def solve_quiz_and_get_code(self):
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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Didn't notice that success message disappears"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.add_to_basket_button).click()

    def book_name(self):
        return self.browser.find_element(*ProductPageLocators.book_name_locator).text

    def book_name_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.book_name_in_basket).text

    def add_to_basket_and_check_name(self):
        book_name = self.book_name()
        self.add_to_basket()
        # self.page.solve_quiz_and_get_code()
        book_name2 = self.book_name_in_basket()
        assert book_name2 == book_name
