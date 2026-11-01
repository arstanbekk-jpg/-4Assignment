def isArmstrong(n):
    a = n // 100
    b = n // 10 % 10
    c = n % 10

    if a**3 + b**3 + c**3 == n:
        return True
    return False


def printArmstrong():
    for i in range(100, 1000):
        if isArmstrong(i):
            print(i, end=" ")


printArmstrong()