def check(nums, m) -> bool:
    if m==1: return True
    i, j = 0, 1
    n = len(nums)
    akt = 1
    while j < n:
        if nums[j-1] < nums[j]:
            j+=1 
            akt += 1
        else:
            i = j
            if i+1 < n: 
                j = i+1
                akt = 1
            else: break
        if akt >= m: return True

    return False 

def solution(nums) -> int:
    l, r = 1, len(nums)

    while l<=r:
        m = (l+r)//2

        if check(nums, m) == True:
            l = m
        else:
            r = m-1
    return l

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    ans = solution(nums)
    print(ans)