from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_CONTENT = (By.CSS_SELECTOR, "div.content div#content_inner p")
    BASKET_CONTENT_LINK = (By.CSS_SELECTOR, "div.content div#content_inner p a")
    EMPTY_BASKET_WORDS = \
        ("سلة التسوق فارغة", "La seva cistella està buida.", "Váš košík je prázdný.",
         "Din indkøbskurv er tom.", "Ihr Warenkorb ist leer.", "Your basket is empty.",
         "Το καλάθι σας είναι άδειο.", "Tu carrito esta vacío.", "Korisi on tyhjä",
         "Votre panier est vide.", "Il tuo carrello è vuoto.", "장바구니가 비었습니다.",
         "Je winkelmand is leeg", "Twój koszyk jest pusty.", "O carrinho está vazio.",
         "Sua cesta está vazia.", "Cosul tau este gol.", "Ваша корзина пуста",
         "Váš košík je prázdny", "Ваш кошик пустий.", "Your basket is empty.")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div#basket_totals th.total")

class LoginPageLocators:
    registration_url = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    login_email = (By.CSS_SELECTOR, 'input#id_login-username')
    login_password = (By.CSS_SELECTOR, "input#id_login-password")
    login_button = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    registration_email = (By.CSS_SELECTOR, 'input#id_registration-email')
    registration_password_1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    registration_password_2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    registration_button = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators:
    add_to_basket_button = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    book_name = (By.CSS_SELECTOR, 'div.product_main h1')
    book_price = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    book_name_in_basket = (By.CSS_SELECTOR, 'div.alertinner strong')
    book_price_in_basket = (By.CSS_SELECTOR, 'div.basket-items p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
