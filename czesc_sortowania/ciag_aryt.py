"""
Szukamy takich podziałów ciągu, że wydzielone elementy utworzą sumy, które utworzą
ciąg arytmetyczny.
"""

def sumy(A: list[int]) -> list:
    pref = [0]*(len(A)+1)
    
    for i in range(len(A)):
        pref[i+1] = pref[i] + A[i]
    return pref


A = [1,2,5,7,3,4,10]
print(sumy(A))