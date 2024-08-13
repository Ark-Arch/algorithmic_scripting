def findBinary(number):

    # base case
    if number == 0:
        return '1'
    else:
        if number % 2 != 0:
            rem = '1'
        elif number % 2 == 0:
            rem = '0'
            
        return findBinary(number//2) + rem


print(findBinary(13))