"""
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

figure_colors = {"square": "#808080", "circle": "#808080", "triangle": "#808080"} # code smell

@app.route('/')
def index():
    return render_template('index.html', figure_colors=figure_colors)

@app.route('/change-color', methods=['POST'])
def change_color():
    data = request.get_json()
    figure_type = data.get('figure_type')
    new_color = data.get('new_color')

    if figure_type:
        # begin - code smell
        if figure_type == "square":
            figure_colors["square"] = new_color
        elif figure_type == "circle":
            figure_colors["circle"] = new_color
        elif figure_type == "triangle":
            figure_colors["triangle"] = new_color
        # end - code smell
        return jsonify({"status": "success", "figure_colors": figure_colors})
    return jsonify({"status": "error", "message": "figure type error"}), 400

@app.route('/change-color-all', methods=['POST'])
def change_color_all():
    data = request.get_json()
    new_color = data.get('new_color')

    if new_color:
        figure_colors["square"] = new_color # code smell
        figure_colors["circle"] = new_color # code smell
        figure_colors["triangle"] = new_color # code smell
        return jsonify({"status": "success", "figure_colors": figure_colors})
    return jsonify({"status": "error", "message": "new color error"}), 400

if __name__ == '__main__':
    app.run(debug=True)
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Definicja klas figur

class Figure:
    def __init__(self, color="#808080"):
        self.color = color

    def set_color(self, new_color):
        self.color = new_color

    def get_color(self):
        return self.color

class Square(Figure):
    pass

class Circle(Figure):
    pass

class Triangle(Figure):
    pass

# Serwis odpowiedzialny za zarządzanie figurami

class FigureService:
    def __init__(self):
        # Inicjalizacja kolekcji figur – kluczem jest typ figury
        self.figures = {
            "square": Square(),
            "circle": Circle(),
            "triangle": Triangle()
        }

    def get_colors(self):
        """Zwraca słownik z kolorami figur."""
        return {name: figure.get_color() for name, figure in self.figures.items()}

    def change_color(self, figure_type, new_color):
        """Zmienia kolor konkretnej figury. Zwraca True, jeśli udało się zmienić, lub False w przeciwnym przypadku."""
        if figure_type in self.figures:
            self.figures[figure_type].set_color(new_color)
            return True
        return False

    def change_all_colors(self, new_color):
        """Ustawia ten sam kolor dla wszystkich figur."""
        for figure in self.figures.values():
            figure.set_color(new_color)

# Inicjalizacja serwisu
figure_service = FigureService()

# Definicje tras Flask

@app.route('/')
def index():
    # Renderujemy szablon, przekazując aktualny stan kolorów z serwisu
    return render_template('index.html', figure_colors=figure_service.get_colors())

@app.route('/change-color', methods=['POST'])
def change_color():
    data = request.get_json()
    figure_type = data.get('figure_type')
    new_color = data.get('new_color')
    if figure_type and new_color:
        if figure_service.change_color(figure_type, new_color):
            return jsonify({"status": "success", "figure_colors": figure_service.get_colors()})
    return jsonify({"status": "error", "message": "figure type error"}), 400

@app.route('/change-color-all', methods=['POST'])
def change_color_all():
    data = request.get_json()
    new_color = data.get('new_color')
    if new_color:
        figure_service.change_all_colors(new_color)
        return jsonify({"status": "success", "figure_colors": figure_service.get_colors()})
    return jsonify({"status": "error", "message": "new color error"}), 400

if __name__ == '__main__':
    app.run(debug=True)
