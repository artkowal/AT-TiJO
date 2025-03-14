class InvalidPinException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class ATM:
    """
    Klasa reprezentujaca bankomat (ATM) z podstawowymi operacjami bankowymi.
    """

    def __init__(self, initial_balance: float, correct_pin: int,):
        self.balance = initial_balance
        self.correct_pin = correct_pin

    def check_balance(self, pin: int) -> float:
        """
        Sprawdza saldo konta uzytkownika.

        :param pin: PIN uzytkownika.
        :return: Saldo konta uzytkownika.
        :raises InvalidPinException: Jesli podany PIN jest nieprawidlowy.
        """
        if pin != self.correct_pin:
            raise InvalidPinException("Nieprawidłowy PIN")
        return self.balance

    def deposit(self, pin: int, amount: float) -> float:
        """
        Wplaca srodki na konto uzytkownika.

        :param pin: PIN uzytkownika.
        :param amount: Kwota do wplacenia.
        :return: Aktualne saldo po wplacie.
        :raises InvalidPinException: Jesli podany PIN jest nieprawidlowy.
        """
        if pin != self.correct_pin:
            raise InvalidPinException("Nieprawidlowy PIN")
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być większa od zera")

        self.balance += amount
        return self.balance

    def withdraw(self, pin: int, amount: float) -> float:
        """
        Wyplaca srodki z konta uzytkownika.

        :param pin: PIN uzytkownika.
        :param amount: Kwota do wyplacenia.
        :return: Aktualne saldo po wyplacie.
        :raises InsufficientFundsException: Jesli saldo jest niewystarczajace.
        :raises InvalidPinException: Jesli podany PIN jest nieprawidlowy.
        """
        if pin != self.correct_pin:
            raise InvalidPinException("Nieprawidłowy PIN")
        if amount <= 0:
            raise ValueError("Kwota wypłaty musi być większa od zera")
        if amount > self.balance:
            raise InsufficientFundsException("Niewystarczające środki na koncie")

        self.balance -= amount
        return self.balance