[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

# Labolatoriun 8: OOP Object-Oriented Programming

---

## OOP

**Programowanie obiektowe** _(ang. Object-Oriented Programming)_ 
to paradygmat programowania, który opiera się na koncepcji obiektów. 
Obiekty są instancjami klas, które definiują ich właściwości i zachowanie. 
Programowanie obiektowe umożliwia tworzenie bardziej złożonych i elastycznych 
aplikacji poprzez organizację kodu w moduły.

### Paradygmaty programowania obiektowego

Programowanie obiektowe opiera się na kilku kluczowych paradygmatach:

- **Abstrakcja:** Proces ukrywania szczegółów implementacji i przedstawiania tylko istotnych cech obiektu;
- **Enkapsulacja:** Proces grupowania danych i metod w jedną jednostkę (klasę) oraz ograniczania dostępu do niektórych jej elementów;
- **Dziedziczenie:** Mechanizm, który pozwala na tworzenie nowych klas na podstawie istniejących, dziedzicząc ich właściwości i metody;
- **Polimorfizm:** Zdolność różnych klas do implementacji tych samych metod, co pozwala na użycie tych samych interfejsów w różnych kontekstach;

### setter()

**setter()** jest odpowiedzialny za zmianę "wnętrza" obiektu. Jeśli zaimplementujesz go niedbale, może narobić bałaganu.
Weryfikuj, czy podajesz sensowne dane, pilnuj, aby wszystko w obiekcie do siebie pasowało po zmianie.
Możesz łatwo "zepsuć" swój obiekt i wprowadzić go w zły stan.

### getter()

**getter()** jest odpowiedzialny za bezpieczny odczyt danych z "wnętrza" 
obiektu. Jeśli zaimplementujesz go niedbale, możesz ujawnić zbyt wiele. 
Getter powinien być prosty, ale przemyślany – upewnij się, że zwraca dane w 
odpowiedniej formie i nie zdradza więcej, niż powinien.


