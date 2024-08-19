left = 19
right = 31

def SieveOfEratosthenes(right):
 

    prime = [True for i in range(right+1)]
    p = 2
    while (p * p <= right):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, right+1, p):
                prime[i] = False
        p += 1
    return prime
 
prime = SieveOfEratosthenes(right)



    

