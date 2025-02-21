# Testowanie i Jakość Oprogramowania

# Asercja

Jest to forma zdaniowa w danym języku, która zwraca prawdę lub fałsz. Asercja wskazuje, 
że programista zakłada, że ów predykat jest w danym miejscu prawdziwy.
W przypadku gdy predykat jest fałszywy (czyli niespełnione są warunki postawione przez programistę)
asercja powoduje przerwanie wykonania programu. Asercja ma szczególne zastosowanie w
trakcie testowania tworzonego oprogramowania.

# Zadanie 1

Zaimplementuj funkcję def max(digits), która wyszuka największy element z tablicy liczb całkowitych (digits).
Zaproponuj dobre testy / asercje:

- Obsługa None (gdy na wejściu pojawi się None to metoda zwraca None).
- Obsługa pustej tablicy (gdy na wejściu pojawi się pusta tablica metoda zwraca None).
- Obsługa tablicy jednoelementowej (metoda zwraca największy element).
- Obsługa tablicy wieloelementowej (metoda zwraca największy element).

# Arrange-Act-Assert (AAA)

Arrange-Act-Assert (AAA) to technika opisu testów, która pomaga w tworzeniu klarownych, czytelnych i zrozumiałych
przypadków testowych. Jest to często stosowany format, który ułatwia organizację testów poprzez podział na trzy etapy:
- przygotowanie warunków początkowych (Arrange), 
- wykonanie testowanej operacji (Act) 
- weryfikację oczekiwanych rezultatów (Assert).

# Zadanie 2

Podziel swój kod (zadanie 1) na kod produkcyjny (pakiet src) i testowy (pakiet test). Asercje powinny znaleźć się w oddzielnych
funkcjach (jedna asercja na funkcję) oraz powinny być zapisane zgodnie z konwencją Arrange-Act-Assert.

# Zadanie 3

Zaimplementuj funkcję def is_perfect(digit), która zweryfikuje, czy podana liczba to liczba doskonała. Zaproponuj dobre testy.
Zastosuj poznane zagadnienia podczas laboratorium.