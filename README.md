# Cryptography-App
App for encrypting files using asymmetric cryptography

ogólna prezentacja:
https://docs.google.com/presentation/d/1_jRYcxByweezk_NpuWrAhXhTVERJH5ok4_XvcDfldB4/edit#slide=id.g1e285bdd49b_0_10

zrobione:
- generowanie kluczy publicznych, prywatnych i generowanie na ich podstawie certyfikatu, podpisywanie (własnoręczne) certyfikatu. Nie wiem jak niby przez centrym certyfikacji to zrobić.
- Aplikacja do szyfrowania i deszyfrowania hybrydowego połączenie kryptografii asymetrycznej (RSA) z kryptografią symetryczną (AES). Plik jest szyfrowany symetrycznie używając losowego wektora inicjalizacyjnego i losowego klucza symetrycznego. Następnie klucz symetryczny jest szyfrowany kluczem publicznym i doklejany do zaszyfrowanego symetrycznie pliku razem z wektorem. W trakcie deszyfrowania pliku wyodrębniany jest wektor inicjalizacyjny oraz zaszyfrowany klucz symetryczny. Zaszyfrowany klucz symetryczny jest deszyfrowany kluczem prywatnym użytkownika. Następnie cała wiadomość jest deszyfrowana symetrycznie. Taki sposób hybrydowy jest szybszy i lepszy dla dużych plików chyba. 
- odczytywanie certyfikatu 
- wyodrębnianie klucza publicznego z certyfikatu


