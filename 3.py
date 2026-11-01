def printInvertedPyramid(n):
    for i in range(n):
        print("*" * (2 * (n - i) - 1))

printInvertedPyramid(3)