def solve(przedmioty: list[tuple], rozmiar): 
    n = len(przedmioty)
    plecak = [[0]*(rozmiar+1) for _ in range(n+1)]

    for przedmiot in range(1, n + 1):
            wartosc = przedmioty[przedmiot-1][0]
            waga = przedmioty[przedmiot-1][1]

            for akt in range(1, rozmiar + 1):
                
                if akt >= waga:
                    nowa_suma = wartosc + plecak[przedmiot-1][akt - waga]
                    
                    plecak[przedmiot][akt] = max(plecak[przedmiot-1][akt], nowa_suma)
                
                else: 
                    plecak[przedmiot][akt] = plecak[przedmiot-1][akt]

    prev = plecak[n][rozmiar]
    w = rozmiar
    used = []
    for i in range(n-1,0,-1):
        if prev != plecak[i-1][w]: 
            used.append(przedmioty[i-1])
            w  = w - przedmioty[i-1][1]
        prev = plecak[i-1][rozmiar]
    
    print(used)
if __name__ == "__main__":
    przedmioty = [(10, 2), (4, 1), (15,3), (1,10), (30,5), (40, 8)]
    rozmiar = 8 
    solve(przedmioty, rozmiar)


def plecak_1d(wagi, wartosci, pojemnosc):
    n = len(wagi)
    dp = [0] * (pojemnosc + 1)
    
    for i in range(n):
        waga = wagi[i]
        wart = wartosci[i]
        
        for w in range(pojemnosc, waga - 1, -1):
            dp[w] = max(dp[w], dp[w - waga] + wart)
            
    return dp[pojemnosc]