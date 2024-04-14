"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(50)
        assert product.check_quantity(500)
        assert product.check_quantity(900)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product_count_buy = 250
        product.buy(product_count_buy)
        assert product.check_quantity(750)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product)
        assert cart.products[product] == 1

        cart.add_product(product, 99)
        assert cart.products[product] == 100

    def test_remove_product(self, product, cart):
        cart.products[product] = 100
        cart.remove_product(product, 1)
        assert cart.products[product] == 99

        cart.remove_product(product, 49)
        assert cart.products[product] == 50

        cart.remove_product(product, 50)
        assert product not in cart.products

        cart.products[product] = 100
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear(self, product, cart):
        cart.products[product] = 100
        cart.clear()
        assert product not in cart.products

    def test_get_total_price(self, product, cart):
        cart.products[product] = 1
        assert cart.get_total_price() == 100

        cart.products[product] = 17
        assert cart.get_total_price() == 1700

        cart.products[product] = 0
        assert cart.get_total_price() == 0

    def test_buy(self, product, cart):
        cart.products[product] = 100
        cart.buy()
        assert product.check_quantity(900)

        cart.products[product] = 901
        with pytest.raises(ValueError):
            cart.buy()
