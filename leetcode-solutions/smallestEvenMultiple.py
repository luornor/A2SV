def smallestEvenMultiple(n: int) -> int:

    if n>2:
        greater = n
    else:
        greater = 2
    while True:
        if(greater % n ==0) and (greater % 2 ==0):
            lcm = greater
            break
        greater += 1
    return lcm


print(smallestEvenMultiple(5))
        


