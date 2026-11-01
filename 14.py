def transformDigits(n):
    v = ""

    for i in str(n):
        if int(i) % 2 == 0:
            v += str(int(i) + 1)
        else:
            v += str(int(i) - 1)

    print(v)


transformDigits(983210)