from math import sqrt

def sieve_of_eratosthenes(n):

    primes = range(3, n + 1, 2) # primes above 2 must be odd so start at three and increase by 2
    
    for base in range(len(primes)):
        if primes[base] is None:
           continue
        if primes[base] >= sqrt(n): # stop at sqrt of n
            break
        for i in range(base + (base + 1) * primes[base], len(primes), primes[base]):
            primes[i] = None
            
    primes.insert(0,2)
    sieve=filter(None, primes)
    return  sieve

def prime_factors(sieve,n):
    p_f = []
    for prime in sieve:
        while n % prime == 0:
            p_f.append(prime)
            n /= prime
    if n > 1:
        p_f.append(n)
    return p_f
    
sieve = sieve_of_eratosthenes(3150)
print (prime_factors(sieve,3150))