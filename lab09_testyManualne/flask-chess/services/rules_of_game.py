class RulesOfGame:
    """
        Metoda zwraca true, tylko gdy przejscie z polozenia source na destination w jednym ruchu jest zgodne
        z zasadami gry w szachy.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")

class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination

class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False

        col_s, row_s = source
        col_d, row_d = destination
        dx = abs(col_s - col_d)
        dy = abs(row_s - row_d)

        # Skoczek kształcie litery L: (1,2) lub (2,1)
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)


class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False

        col_s, row_s = source
        col_d, row_d = destination
        dx = abs(col_s - col_d)
        dy = abs(row_s - row_d)

        return (dx == 0 and dy != 0) or (dy == 0 and dx != 0)

class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False

        col_s, row_s = source
        col_d, row_d = destination
        dx = abs(col_s - col_d)
        dy = abs(row_s - row_d)

        # Hetman = wieża (prosto) lub goniec (skos)
        straight = (dx == 0 and dy != 0) or (dy == 0 and dx != 0)
        diagonal = (dx == dy and dx != 0)
        return straight or diagonal


class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False

        col_s, row_s = source
        col_d, row_d = destination
        dx = abs(col_s - col_d)
        dy = abs(row_s - row_d)

        # Król jedno pole we wszystkich kierunkach
        return max(dx, dy) == 1

class Pawn(RulesOfGame):
    def __init__(self, is_white=True):
        self.is_white = is_white

    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False

        col_s, row_s = source
        col_d, row_d = destination
        dx = col_d - col_s
        dy = row_d - row_s
        direction = 1 if self.is_white else -1

        # 1) Jedno pole do przodu
        if dx == 0 and dy == direction:
            return True

        # 2) Start: dwa pola do przodu
        start_row = 2 if self.is_white else 7
        if dx == 0 and dy == 2 * direction and row_s == start_row:
            return True

        # 3) bicia na ukos: jedno pole na skos
        if abs(dx) == 1 and dy == direction:
            return True

        return False