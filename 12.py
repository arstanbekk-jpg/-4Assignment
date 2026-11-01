def reverseNumber(n):
    r = ""
    while n > 0:
        l = n % 10
        r += str(l)
        n //= 10
    print(r)
reverseNumber(1234)