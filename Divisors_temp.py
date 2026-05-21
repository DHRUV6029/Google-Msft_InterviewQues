def find_divisors(n):
    divisors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:          # avoid duplicate for perfect squares
                divisors.append(n // i)
    
    return sorted(divisors)
