def decimalToBinary(n):
    b = ""
    while n > 0:
        l = n % 2
        b = str(l) + b
        n = n // 2
    print(b)

decimalToBinary(13)