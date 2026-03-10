"""
Jest dana tablica z liczba, sprawdz czy istnieje liczba x ktory wystepuje >= n/2 razy
"""

def solve_no_stack(A: list[int]) -> int | None:
    
    counter: int = 0
    lead: int | None = None

    for num in A:
        
        if counter==0:
            lead = num
            counter+=1
        elif num==lead:
            counter+=1
        else:
            counter-=1

    if counter==0:
        return None
    
    count_lead = 0

    for num in A:
        if num==lead: count_lead+=1

    if count_lead > len(A)//2:
        return lead
    return None

def solve_stack(A: list[int]) -> int | None:

    stos = []

    for num in A:

        if len(stos)==0:
            stos.append(num)
        
        elif stos[-1]!=num:
            stos.pop()
        else:
            stos.append(num)

    lider = stos[0]
    count = 0
    for num in A:
        if num == lider:count+=1

    if count > len(A)//2:
        return lider
    return None

if __name__ == "__main__":
    A = [1, 2, 1, 2, 1]
    lider = solve_stack(A)
    if lider == None:
        print(f"brak lidera")
    else:
        print(f"lider to {lider}")
