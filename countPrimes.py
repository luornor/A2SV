def count_primes(n):
    prime_count = 0
    is_prime = [True]*n
    is_prime[0]=False
    is_prime[1]=False
    for i in range(2,n):    
        if is_prime[i]: #take each item in prime list
            for j in range(i*i,n,i): #mark all its multiples
                is_prime[j]=False    
            prime_count+=1
    print(prime_count)




n = int(input())
count_primes(n)