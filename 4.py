def printMatrix(n, m):
    count = 1

    for i in range(n):
        for j in range(m):
            print(count, end=" ")
            count += 1
        print()

printMatrix(2, 3)