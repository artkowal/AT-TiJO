class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer


class OrderValidator:
    @staticmethod
    def validate(order):
        print("Walidacja zamówienia.")


class OrderRepository:
    @staticmethod
    def save(order):
        print("Zapisywanie zamówienia do bazy danych.")


class EmailService:
    @staticmethod
    def send_confirmation(order):
        print("Wysyłanie e-maila potwierdzającego.")


class OrderProcessor:
    def __init__(self, order):
        self.order = order
        self.validator = OrderValidator()
        self.repository = OrderRepository()
        self.email_service = EmailService()

    def process_order(self):
        self.validator.validate(self.order)
        self.repository.save(self.order)
        self.email_service.send_confirmation(self.order)


order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
processor = OrderProcessor(order)
processor.process_order()
