from pages.main_page import MainPage
from pages.login_page import LoginPage

link1 = "http://selenium1py.pythonanywhere.com/"

'''def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link1)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link1)
    page.open()
    page.should_be_login_link()'''

def test_login_form_should_be_present(browser):
    page = LoginPage(browser, link1)
    page.open()
    page.click_login_link()
    page.should_be_login_page()
