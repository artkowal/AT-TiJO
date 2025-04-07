from abc import ABC, abstractmethod

class ILunarRover(ABC):
    """
    Interfejs (klasa abstrakcyjna) pojazdu księżycowego.
    Zawiera metody wymagane do obsługi ruchu w przestrzeni 2D.
    """

    @abstractmethod
    def move_forward(self, steps: int):
        """Przemieszcza pojazd o 'steps' pól w przód."""
        pass

    @abstractmethod
    def move_backward(self, steps: int):
        """Przemieszcza pojazd o 'steps' pól w tył."""
        pass

    @abstractmethod
    def rotate_left(self):
        """Obraca pojazd o 90 stopni w lewo."""
        pass

    @abstractmethod
    def rotate_right(self):
        """Obraca pojazd o 90 stopni w prawo."""
        pass

    @abstractmethod
    def get_position(self) -> tuple:
        """
        Zwraca aktualną pozycję (x, y) pojazdu.
        """
        pass

    @abstractmethod
    def get_orientation(self) -> str:
        """
        Zwraca aktualne zorientowanie pojazdu w formie np. 'N', 'E', 'S', 'W'.
        """
        pass
