def isPalindrome(string):
    string = ''.join(char for char in string if char.isalnum()).lower()

    n = len(string)
    # base case
    if n < 2:
        return True
    elif (string[0] == string[n-1]):
        return isPalindrome(string[1:n-1])
    
    else:
        return False

print(isPalindrome('raCe:::a car!'))
