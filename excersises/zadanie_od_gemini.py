"""
Zadanie: K-ty Najtańszy Zestaw Rolniczy (K-th Smallest Pair Sum)Pługosław i Rzepisław idą na zakupy do lokalnego dealera sprzętu.
Pługosław ma w ręku posortowany cennik $N$ modeli traktorów (tablica A). Rzepisław ma posortowany cennik $N$ modeli przyczep (tablica B).
Bracia chcą kupić dokładnie jeden zestaw (jeden traktor + jedna przyczepa). 
Z racji tego, że decyzje podejmują losowo, chcą przygotować sobie listę wszystkich możliwych opcji zakupu. Gdyby wypisać wszystkie możliwe kombinacje i je posortować od najtańszej do najdroższej, powstałaby ogromna lista zestawów.
Ojciec poprosił ich o podanie tylko i wyłącznie $K$-tego najtańszego zestawu z tej wielkiej listy (czyli szukamy $K$-tej najmniejszej sumy $A[i] + B[j]$).Haczyki i wymagania:Długość list $N$ wynosi do $100\ 000$.Wartość $K$ też może wynosić do $100\ 000$.
Jeśli zrobisz to "brutalnie" (czyli wyliczysz wszystkie pary dwiema pętlami for, wrzucisz do tablicy i posortujesz), wykonasz $N \times N = 10\ 000\ 000\ 000$ (10 miliardów) operacji.
Złożoność $O(N^2 \log(N^2))$ absolutnie obleje testy czasowe i zje całą pamięć.
Cel:Musisz znaleźć ten $K$-ty najtańszy zestaw w czasie $O(K \log K)$, używając Min-Kopca.
Musisz wyciągać zestawy płynnie, nie generując całej reszty.
"""

