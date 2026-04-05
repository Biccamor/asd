
def counting(nums):
    m = max(nums)
    count = [0]*(m+1)
    n = len(nums)

    for i in nums:
        count[i]+=1

    if n%2==0:
        high = n//2
        low = n//2 
    else:
        high = n//2
        low = n//2 + 1
    idx_high = 1
    idx_low = 0

    print(count)
    for i in range(len(count)-1,-1,-1):
        while count[i] > 0:
            if high >0:
                nums[idx_high] = i
                idx_high -= 2
                count[i]-=1
                high -= 1
            else:
                nums[idx_low] = i
                idx_low -= 2
                count[i] -= 1 
                low -= 1


if __name__ == "__main__":

    nums = [4,5,5,6]
    # 4  5  5 6 
    counting(nums)
    print(nums)


            
            