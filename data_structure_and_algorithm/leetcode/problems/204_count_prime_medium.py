n = 15

def count_primes(n) -> int:
    count = 0
    if n > 1:
        for i in range(n):
            if (i % i == 1 and i % 1 == i):
                count += 1
    return count

count_primes(n)