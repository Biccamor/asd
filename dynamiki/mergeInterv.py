def merge(intervals):
    intervals.sort(key=lambda x: (x[0], x[1]))
    inter_s = intervals[0][0]
    prev_e = intervals[0][1]
    ans = []

    for s,e in intervals[1:]: 
        if s <= prev_e: 
            prev_e = max(prev_e, e)
        else:
            
            ans.append([inter_s, prev_e])
            inter_s = s
            prev_e = e 
    
    ans.append([inter_s, prev_e])


    return ans

inter = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
print(merge(inter))