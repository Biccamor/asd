def findMaximizedCapital(k: int, w: int, profits, capital) -> int:
    import heapq as hq 
    q_prof = []
    q_cap = []
    n = len(profits)
    for i in range(n):
        if capital[i] > w:
            hq.heappush(q_cap, (capital[i], profits[i]))
            continue 
        hq.heappush(q_prof, -profits[i])

    akt_w = w 
    for i in range(k):
        if len(q_prof)==0: break
        neg_prof = hq.heappop(q_prof)
        prof = -neg_prof
        akt_w += prof
        while True:
            if len(q_cap) == 0: break 
            cap, prof = hq.heappop(q_cap)
            if cap <= akt_w:
                hq.heappush(q_prof, -prof)
            else:
                hq.heappush(q_cap, (cap, prof))
                break 
    return akt_w
 
k =3
w =0
profits =[1,2,3]
capital =[0,1,2]
print(findMaximizedCapital(k,w,profits,capital))