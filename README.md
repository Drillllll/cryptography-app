# Cryptography-App
App for encrypting files using asymmetric cryptography

ogólna prezentacja:
https://docs.google.com/presentation/d/1_jRYcxByweezk_NpuWrAhXhTVERJH5ok4_XvcDfldB4/edit#slide=id.g1e285bdd49b_0_10

zrobione:
- generowanie kluczy publicznych, prywatnych i generowanie na ich podstawie certyfikatu, podpisywanie (własnoręczne) certyfikatu. Nie wiem jak niby przez centrym certyfikacji to zrobić.
- Aplikacja do szyfrowania i deszyfrowania hybrydowego połączenie kryptografii asymetrycznej (RSA) z kryptografią symetryczną (AES). Plik jest szyfrowany symetrycznie używając losowego wektora inicjalizacyjnego i losowego klucza symetrycznego. Następnie klucz symetryczny jest szyfrowany kluczem publicznym i doklejany do zaszyfrowanego symetrycznie pliku razem z wektorem. W trakcie deszyfrowania pliku wyodrębniany jest wektor inicjalizacyjny oraz zaszyfrowany klucz symetryczny. Zaszyfrowany klucz symetryczny jest deszyfrowany kluczem prywatnym użytkownika. Następnie cała wiadomość jest deszyfrowana symetrycznie. Taki sposób hybrydowy jest szybszy i lepszy dla dużych plików chyba. 
- odczytywanie certyfikatu 
- wyodrębnianie klucza publicznego z certyfikatu

do zrobienia:
- Demonstracja, że poufność danych jest rzeczywiście chroniona kryptograficznie, porównanie z ochroną systemową praw dostępu
- generowanie klucza zapasowego/awaryjnego
- znalezienie miejsca na bezpieczne przechowywanie klucza publicznego bo teraz to jest do dupy. Mozna by niby go szyfrowac symetrycznie haslem uzytkownika ale to sie mija z idea szyfrowania asymetrycznego w którym uzytkonik nie musi pamietac zadnych hasel

nad tym trzeba pomyśleć:
- czy jest możliwość generowania certyfikatu przez centrum certyfikacji?
- dlaczego gdy próbujemy deszyfrować plik niepoprawnym kluczem prywatnym to wyrzucany jest błąd? Czy nie powinno być tak, że proces deszyfrowania powiedzie się, ale plik będzie nieczytelny? ( w sensie źle zdeszyfrowany)
- co jesli któryś bajt w zaszyfrowanym pliku ulegnie uszkodzeniu?

