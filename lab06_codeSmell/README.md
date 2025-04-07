[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

# Labolatoriun 6: Code Smells

---

## Code Smell

**Code Smell** to termin używany w programowaniu do opisywania pewnych cech kodu źródłowego,
które wskazują na potencjalne problemy z jego jakością. Niekoniecznie oznaczają one błędy,
ale często prowadzą do trudniejszego utrzymania, rozszerzania i testowania kodu.


### Code Smells wewnątrz klasy

- **Komentarze (_Comments_)** – Czy komentarze są rzeczywiście potrzebne? Powinny wyjaśniać "dlaczego", a nie "co". Jeśli możesz, przekształć kod tak, aby komentarze nie były konieczne. 
- **Długa metoda (_Long Method_)** – Krótsze metody są łatwiejsze do czytania, zrozumienia i debugowania. Jeśli możesz, podziel długą metodę na mniejsze. 
- **Długa lista parametrów (_Long Parameter List_)** – Im więcej parametrów ma metoda, tym bardziej jest skomplikowana. Staraj się ograniczać ich liczbę lub grupować je w obiekty. 
- **Duplikacja kodu (_Duplicated Code_)** – Powtarzający się kod to problem, który należy eliminować. Zasada DRY (Don't Repeat Yourself). 
- **Złożoność warunków (_Conditional Complexity_)** – Unikaj rozbudowanych bloków warunkowych. Możesz rozważyć wzorce projektowe, takie jak dekorator, strategia czy stan. 
- **Eksplozja kombinatoryczna (_Combinatorial Explosion_)** – Jeśli masz wiele podobnych fragmentów kodu, rozważ użycie generyków lub wzorca interpreter. 
- **Zbyt duża klasa (_Large Class_)** – Duże klasy są trudne do czytania i zrozumienia. Sprawdź, czy klasa nie ma zbyt wielu odpowiedzialności. 
- **Typ w nazwie (_Type Embedded in Name_)** – Unikaj umieszczania typów w nazwach metod. 
- **Nieczytelna nazwa (_Uncommunicative Name_)** – Czy nazwa metody jasno mówi, co ona robi? Jeśli nie, zmień ją na bardziej czytelną. 
- **Niespójne nazwy (_Inconsistent Names_)** – Stosuj jednolitą terminologię w całym kodzie. 
- **Martwy kod (_Dead Code_)** – Usuwaj nieużywany kod. Od tego są systemy kontroli wersji. 
- **Spekulatywna ogólność (_Speculative Generality_)** – Pisz kod rozwiązujący obecne problemy, a nie potencjalne przyszłe scenariusze (YAGNI - You Ain’t Gonna Need It).
- **Nietypowe rozwiązanie (_Oddball Solution_)** – Dla tego samego problemu powinna istnieć jedna metoda rozwiązania. 
- **Tymczasowe pola (_Temporary Field_)** – Jeśli obiekt zawiera wiele opcjonalnych pól, sprawdź, czy rzeczywiście są potrzebne.

### Code Smells pomiędzy klasami

- **Alternatywne klasy z różnymi interfejsami (_Alternative Classes with Different Interfaces_)** – Jeśli dwie klasy są wewnętrznie podobne, ale mają różne interfejsy, rozważ wprowadzenie wspólnego interfejsu. 
- **Obsesja na punkcie prymitywów (_Primitive Obsession_)** – Nie używaj wielu zmiennych typu podstawowego zamiast dedykowanej klasy. 
- **Klasa przechowująca tylko dane (_Data Class_)** – Unikaj klas, które jedynie przechowują dane, bez metod operujących na nich. 
- **Nagromadzenie danych (_Data Clumps_)** – Jeśli pewne dane zawsze pojawiają się razem, rozważ utworzenie klasy grupującej te dane. 
- **Odrzucone dziedziczenie (_Refused Bequest_)** – Jeśli klasa dziedziczy po innej, ale nie używa jej funkcjonalności, być może nie powinna korzystać z dziedziczenia. 
- **Nadmierna intymność (_Inappropriate Intimacy_)** – Klasy nie powinny znać swoich wewnętrznych szczegółów nawzajem. 
- **Nieodpowiednia ekspozycja (_Indecent Exposure_)** – Unikaj niepotrzebnego udostępniania elementów klasy na zewnątrz. 
- **Zazdrość o funkcje (_Feature Envy_)** – Jeśli metoda nadmiernie korzysta z innej klasy, powinna się w niej znajdować. 
- **Bezużyteczna klasa (_Lazy Class_)** – Każda klasa powinna mieć istotną funkcję w projekcie. 
- **Łańcuchy wywołań (_Message Chains_)** – Unikaj długich sekwencji wywołań metod. 
- **Zbędny pośrednik (_Middle Man_)** – Jeśli klasa jedynie deleguje pracę innym, może być zbędna. 
- **Rozbieżna zmiana (_Divergent Change_)** – Jeśli jedna klasa wymaga częstych zmian w różnych, niezwiązanych częściach, może mieć zbyt wiele odpowiedzialności. 
- **Rozproszona modyfikacja (_Shotgun Surgery_)** – Jeśli zmiana w jednej klasie wymusza zmiany w wielu innych, spróbuj ograniczyć wpływ zmian do jednej klasy. 
- **Równoległe hierarchie dziedziczenia (_Parallel Inheritance Hierarchies_)** – Jeśli każda nowa klasa wymaga utworzenia innej klasy w innym hierarchicznym drzewie, być może warto uprościć strukturę. 
- **Niekompletna klasa biblioteczna (_Incomplete Library Class_)** – Jeśli biblioteka nie oferuje potrzebnej metody i nie możesz jej zmodyfikować, spróbuj ją wydzielić osobno. 
- **Rozrastające się rozwiązanie (_Solution Sprawl_)** – Jeśli do wykonania jednej rzeczy potrzebujesz pięciu klas, być może projekt jest zbyt skomplikowany.

