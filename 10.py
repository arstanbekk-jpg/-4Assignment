def gcd(a, b):
    cd = 0

    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            cd = i

    return cd


print(gcd(24, 36))