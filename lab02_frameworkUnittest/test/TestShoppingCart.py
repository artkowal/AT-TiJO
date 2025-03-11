import unittest
from lab02_frameworkUnittest.src.ShoppingCart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        print("* setUp()")
        self.cart = ShoppingCart()

    def test_add_product(self):
        print("** test_add_product()")

        # Arrange
        product, price, quantity = "Apple", 5, 3

        # Act
        result = self.cart.add_product(product, price, quantity)

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.products[product], (price, quantity))

    def test_remove_product(self):
        print("** test_remove_product()")

        # Arrange
        self.cart.add_product("Banana", 5, 2)

        # Act
        result = self.cart.remove_product("Banana")

        # Assert
        self.assertTrue(result)
        self.assertNotIn("Banana", self.cart.products)

    def test_update_quantity(self):
        print("** test_update_quantity()")

        # Arrange
        self.cart.add_product("Peach", 5, 4)

        # Act
        result = self.cart.update_quantity("Peach", 10)

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.products["Peach"], (5, 10))

    def test_update_quantity_to_zero(self):
        print("** test_update_quantity_to_zero()")

        # Arrange
        self.cart.add_product("Grapes", 7, 5)

        # Act
        result = self.cart.update_quantity("Grapes", 0)

        # Assert
        self.assertTrue(result)
        self.assertNotIn("Grapes", self.cart.products)

    def test_get_products(self):
        print("** test_get_products()")

        # Arrange
        self.cart.add_product("Dragon fruit", 20, 2)
        self.cart.add_product("Melon", 10, 1)

        # Act
        products = self.cart.get_products()

        # Assert
        self.assertIn("Dragon fruit", products)
        self.assertEqual(len(products), 2)
        #self.assertEqual(len(products), 1)

    def test_count_products(self):
        print("** test_count_products()")

        # Arrange
        self.cart.add_product("Dragon fruit", 20, 2)
        self.cart.add_product("Melon", 8, 4)

        # Act
        count = self.cart.count_products()

        # Assert
        self.assertEqual(count, 2)  # Tylko dwa różne produkty

    def test_get_total_price(self):
        print("** test_get_total_price()")

        # Arrange
        self.cart.add_product("Dragon fruit", 20, 2)
        self.cart.add_product("Melon", 8, 4)

        # Act
        total_price = self.cart.get_total_price()

        # Assert
        expected_price = (20 * 2) + (8 * 4)
        self.assertEqual(total_price, expected_price)

    def test_apply_discount_code(self):
        print("** test_apply_discount_code()")

        # Arrange
        self.cart.add_product("Melon", 8, 7)

        # Act
        result = self.cart.apply_discount_code("DISCOUNT10")
        discount_price = self.cart.get_total_price()

        # Assert
        expected_price = int((8 * 7) * 0.9)  # 10% zniżki
        self.assertTrue(result)
        self.assertEqual(discount_price, expected_price)

    def test_checkout_success(self):
        print("** test_checkout_success()")

        # Arrange
        self.cart.add_product("Dragon fruit", 20, 2)

        # Act
        result = self.cart.checkout()

        # Assert
        self.assertTrue(result)

    def test_checkout_empty_cart(self):
        print("** test_checkout_empty_cart()")

        # Arrange
        self.cart.products.clear()
        #self.cart.add_product("Dragon fruit", 20, 2)

        # Act
        result = self.cart.checkout()

        # Assert
        self.assertFalse(result)

    def tearDown(self):
        print("* tearDown()")
        self.cart = None

if __name__ == '__main__':
    unittest.main()
