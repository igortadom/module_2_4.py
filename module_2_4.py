numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
i = 0
primes = []
not_primes = []
numbers.remove(1)
for i in numbers:
    c = 0
    for j in range(1, i +1):
        if i % j == 0:
           c += 1
    if c == 2:
       primes.append(i)
    else:
       not_primes.append(i)
print(not_primes)
print(primes)






















































