class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.discount = 0

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        """Dodawanie produktu do koszyka"""
        if price < 0 or quantity < 0:
            return False

        if product_name in self.products:
            self.products[product_name] = (price, self.products[product_name][1] + quantity)
        else:
            self.products[product_name] = (price, quantity)

        return True

    def remove_product(self, product_name: str) -> bool:
        """Usuwanie produktu z koszyka"""
        if product_name in self.products:
            del self.products[product_name]
            return True
        return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        """Aktualizacja ilości produktu w koszyku"""
        if product_name in self.products:
            if new_quantity > 0:
                self.products[product_name] = (self.products[product_name][0], new_quantity)
            else:
                del self.products[product_name]
            return True
        return False

    def get_products(self):
        """Pobieranie nazw produktów z koszyka"""
        return list(self.products.keys())

    def count_products(self) -> int:
        """Pobieranie liczby produktów w koszyku"""
        return len(self.products)

    def get_total_price(self) -> int:
        """Pobieranie sumy cen produktów w koszyku"""
        total = sum(price * quantity for price, quantity in self.products.values())
        return int(total * (1 - self.discount / 100))

    def apply_discount_code(self, discount_code: str) -> bool:
        """Zastosowanie kuponu rabatowego"""
        discounts = {"DISCOUNT10": 10, "DISCOUNT20": 20}
        if discount_code in discounts:
            self.discount = discounts[discount_code]
            return True
        return False

    def checkout(self) -> bool:
        """Realizacja zamówienia"""
        return len(self.products) > 0
