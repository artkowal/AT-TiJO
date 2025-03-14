[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

# Labolatoriun 2: _Framework *unittest*_

---

## Struktura testów

- W pierwszej kolejności importujemy bibliotekę unittest, która zawiera funkcje do testowania;
- Każdy test jednostkowy w **unittest** musi być zawarty w klasie, która dziedziczy po **unittest.TestCase**;
- Metoda **setUp()** jest wywoływana przed każdym testem. Jest to miejsce, gdzie inicjalizujemy obiekty lub zasoby, które będą używane w testach;
- Każda metoda testowa musi zaczynać się od **test_**. Jest to konwencja, którą **unittest** wykorzystuje do rozpoznawania metod, które są testami. Każda metoda testowa sprawdza jedną, konkretną funkcjonalność. W przypadku nieprawidłowego wyniku, test zakończy się błędem;
- **assertEqual()** jest to najczęściej używana metoda do porównywania oczekiwanego wyniku z wynikiem rzeczywistym. Sprawdza, czy oba argumenty są sobie równe. Jeśli tak, test przechodzi pomyślnie, w przeciwnym razie test się nie powiedzie;
- **assertRaises()** jest używana do testowania, czy w odpowiednich sytuacjach jest rzucany wyjątek. W tym przypadku sprawdzamy, czy przy próbie dzielenia przez zero zostanie rzucony wyjątek **ValueError**;
- **tearDown() jest wywoływana po każdym teście i służy do usuwania zasobów lub zamykania połączeń, jeśli to konieczne**;
- Testy w **unittest** uruchamiamy za pomocą komendy unittest.main(), co powoduje automatyczne wykrycie i uruchomienie wszystkich metod testowych w klasie.