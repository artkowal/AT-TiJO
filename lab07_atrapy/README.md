[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

# Labolatoriun 7: Atrapy

---

## Atrapy

W testach jednostkowych często spotykamy się z sytjacją, gdzie metoda, którą testujemy,
zależy od innej klasy lub modułu. Nie zawsze jednak chcemy (lub możemy) testować całą
aplikację naraz. W takich przypadkach używa się atrap (**stub, mock**),
czyli obiektów zastępczych symulujących rzeczywiste zachowanie.

### Do czego służą atrapy ?

Atrapy pozwalają nam:

- testować kod bez faktycznej implementacji zależności;
- uniknąć wywołań rzeczywistych operacji, np. zapytań do bazy, API, czy obliczeń;
- skupić się na samej logice testowanej funkcji;

W pythonie do tworzenia atrap wykorzystujemy moduł **unittest.mock**, a w szczególności **Mock()**

### Co to jest Mock() ?

Obiekt **Mock()** jest dynamiczną atrapą, która udaje prawdziwy obiekt i pozwala kontrolować
jego zwracane wartości oraz sprawdzać, czy był wywoływany.

Możemy np.:

- Ustawić wartość zwracaną przez funkcję **(mock.return_value = 42)**;
- Sprawdzić, ile razy była wywołana **(mock.call_count)**,
- zweryfikować z jakimi argumentami była wywołana **(mock.assert_called_with("Hello"))**;

### Przykład
_*example_

Mamy klasę **Counter**, która używa klasy **Operation**. Nie mamy implementacji **count()**,
ale chcemy przetestować **Counter**. Zastosujemy **Mock()** jako atrapę zamiast faktycznej klasy **Operation**.

Następnie zaimplementujemy **testy**, które nie wymagają rzeczywistej implementacji metody **count()**.


