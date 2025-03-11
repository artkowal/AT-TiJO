[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

# TDD - _Test-Driven Development_

---

## TDD - _Test-Driven Development_

**TDD**, czyli **Test-Driven Development** jest to technika tworzenia
oprogramowania, w której najpierw tworzone są testy dla nowej funkcjonalności \ wymagania,
a dopiero później implementowana jest sama funkcjonalność, aby testy przeszły pomyślnie.

Proces tes składa się z 3 głównych kroków:
- **RED:** Napisz testy (testy nie przechodzą, brak implementacji funkcjonalności);
- **GREEN:** Dodaj **minimalną** implementację, aby testy się powiodły;
- **REFACTOR** Zrefaktoryzuj kod do najprostszej implementacji, aby spełniał oczekiwania standardy (testy przechodzą);

Technika została stworzona przez _Kenta Becka_

## Konwencje nazewnicze

### Jasne i opisowe nazwy

- Nazwy testów powinny dokładnie opisywać, co testują;
- Używaj konwencje **test_nazwa_funkcji_lub_metody_should_opis_zachowania**;

### Używaj słów kluczowych

- Słowa takie jak **should, whe, given, then** pomagają w zrozumieniu kontekstu testu;

### Unikaj ogólników

- Utrzymuj spójność w nazewnictwie testów w całym projekcie;

