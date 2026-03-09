""""
Funckja porownujaca elementy w tablicy n elementowej, ma znalezc max i min w 3n/2 porownan
"""

def solve(tab: list[int]) -> tuple[int,int]:
    
    n = len(tab)
    if n == 0: return None
    
    if n % 2 != 0:
        mini = maxi = tab[0]
        start_idx = 1
    else:
        if tab[0] > tab[1]:
            maxi, mini = tab[0], tab[1]
        else:
            maxi, mini = tab[1], tab[0]
        start_idx = 2

    
    for i in range(start_idx,len(tab), 2):
        a = tab[i]
        b = tab[i+1]

        if a>b:
            maxi = max(maxi, a)
            mini = min(mini, b)
        else:
            maxi = max(maxi,b)
            mini = min(mini, a)
    return (mini,maxi)

if __name__ == "__main__":
    
    tab = [10,13,413,33,31,13,5,124]
    mini, maxi = solve(tab)
    print(f"min {mini} max {maxi}")