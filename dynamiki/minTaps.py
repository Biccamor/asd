
def minTaps(n: int, ranges) -> int:
    inter = [0]*(n+1)

    for i, r in enumerate(ranges):
        start = max(0, i - r)
        end = min(n, i + r)
        inter[start] = max(inter[start], end)
    print(inter)
    max_dist = inter[0]
    ans = 1
    new_dist = 0
    for i in range(1, len(inter)):
        
        if i > max_dist: return -1

        if max_dist == n: return ans

        new_dist = max(inter[i], new_dist)
        if i == max_dist:
            max_dist = new_dist
            ans += 1

    if max_dist == n:
        return ans
    return -1
n = 4
ranges = [0,0,0,0]


print(minTaps(n,ranges))