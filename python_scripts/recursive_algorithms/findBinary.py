def findBinary(number, track = False):
    # base case
    if (number == 0):
        if track:
            return ''
        else:
            return '0'
    else:
        track = True
        if number % 2 != 0:
            rem = '1'
        elif number % 2 == 0:
            rem = '0'
            
        return findBinary(number//2, track) + rem


print(findBinary(233)) # == 1 0 1