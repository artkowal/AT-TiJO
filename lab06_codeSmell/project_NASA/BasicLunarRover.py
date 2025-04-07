from lab06_codeSmell.project_NASA.ILunarRover import ILunarRover

class BasicLunarRover(ILunarRover):
    """
    Przykładowa implementacja pojazdu księżycowego.
    Pojazd porusza się w przestrzeni 2D, posiada orientację
    (N, E, S, W) oraz aktualną pozycję (x, y).
    """

    ORIENTATIONS = ['N', 'E', 'S', 'W']  # Ustalona kolejność do obrotów

    def __init__(self, start_x=0, start_y=0, start_orientation='N'):
        self.x = start_x
        self.y = start_y

        if start_orientation not in self.ORIENTATIONS:
            raise ValueError("Niewłaściwa orientacja początkowa.")
        self.orientation = start_orientation

    def move_forward(self, steps: int):
        if steps < 0:
            raise ValueError("Liczba kroków nie może być ujemna w move_forward.")
        if self.orientation == 'N':
            self.y += steps
        elif self.orientation == 'S':
            self.y -= steps
        elif self.orientation == 'E':
            self.x += steps
        elif self.orientation == 'W':
            self.x -= steps

    def move_backward(self, steps: int):
        if steps < 0:
            raise ValueError("Liczba kroków nie może być ujemna w move_backward.")
        # move_backward - ruch w przeciwnym kierunku do aktualnej orientacji
        if self.orientation == 'N':
            self.y -= steps
        elif self.orientation == 'S':
            self.y += steps
        elif self.orientation == 'E':
            self.x -= steps
        elif self.orientation == 'W':
            self.x += steps

    def rotate_left(self):
        # Obracamy o 90 stopni w lewo
        current_index = self.ORIENTATIONS.index(self.orientation)
        # Przesunięcie w lewo (-1)
        self.orientation = self.ORIENTATIONS[(current_index - 1) % len(self.ORIENTATIONS)]

    def rotate_right(self):
        # Obracamy o 90 stopni w prawo
        current_index = self.ORIENTATIONS.index(self.orientation)
        # Przesunięcie w prawo (+1)
        self.orientation = self.ORIENTATIONS[(current_index + 1) % len(self.ORIENTATIONS)]

    def get_position(self) -> tuple:
        return (self.x, self.y)

    def get_orientation(self) -> str:
        return self.orientation
