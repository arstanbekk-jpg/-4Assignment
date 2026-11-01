def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

isPalindrome(121)