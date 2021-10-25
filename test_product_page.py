import pytest
from pages.product_page import ProductPage

link_1 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
links = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}" for n in range(10)]

@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    print(link)
    page = ProductPage(browser, link)
    page.open()
    book_name = page.book_name()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    book_name2 = page.book_name_in_basket()
    assert book_name2 == book_name

@pytest.mark.xfail(reason="Success message should certainly be present", strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Correct behavior", strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()