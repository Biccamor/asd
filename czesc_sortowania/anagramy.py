# Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, każde nad alfabetem długości k,
# sprawdza czy A i B są swoimi anagramami.
# 1. Proszę zaproponować rezwiązanie działające w czasie O(n+k)
# 2. Proszę zaproponować rozwiązanie działające w czasie O(n) (proszę zwrócić uwagę, że k może być dużo większe od 
# np. dla alfabetu UNICODE; złożoność pamięciowa może być rzędu)


def rozwiazanie1(A,B,k): 
    n = len(A)
    countA = [0]*k
