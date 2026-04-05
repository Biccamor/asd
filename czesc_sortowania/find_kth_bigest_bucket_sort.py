def bucket_sort(A,k):
    n = len(A)
    bucket = [[] for _ in range(n)]
    maxi = max(A)
    mini = min(A)
    size = (maxi-mini)//n

    for el in A:
        idx = el//size 
        bucket[idx].append(el)
     


def main():
    A = [10,1,3,4,23,5,65,7]
    k = 4