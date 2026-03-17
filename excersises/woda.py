"""
Woda spływa z kranu do zbiorników, które są połączone rurami.
Zbiornik jest opisany krotką z górną i dolną wysokością danego zbiornika (górna jest pierwsza).
Pole przekroju danego zbiornika to 1 m2. Woda zawsze spłynie na sam dół.
Mamy podaną ilość m3 wody jako l i mamy podać, do jakiej wysokości woda zapełni zbiorniki.
Wysokości są zmiennoprzecinkowe.

Przykladowy input

(10,4), (11,3), (7,2)...
"""

def check(A, h):
    """
    Sprawdzamy ile litrow wody bedzie dla h wysokosci
    """
    ans = 0
    for a,b in A: 
        
        if h>=a:
            ans += a-b 
        if h<a and h>b:
            ans += h-b
        if h<b:
            continue
    return ans

def bisect(A, w):
    eps = 1e-11
    l, h= 0, max(A, key=lambda x: x[0])[0]
    m = 0
    while h-l>=eps:
        m = (l+h)/2

        if check(A,m) < w:
            l = m 
        else:
            h = m
    return m

if __name__ == "__main__":

    T = [(2.5, 0.0), (4.2, 1.5), (8.1, 6.0)]
    print(bisect(T, 5.3))
