def count_primes(n):
    n_list = [i for i in range(1,n)]
    lenght = len(n_list)
    modulo = 2
    countPrimes = []
    print(n_list)
    for item in n_list[1:]:
        if item==2:
            countPrimes.append(item)
        else:
            if item%modulo==0:
                n_list.remove(item)
                modulo+=1

            
    return countPrimes.count()

print(count_primes(10))
