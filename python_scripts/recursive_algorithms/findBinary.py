#### METHOD ONE ###########
def findBinary(number, track = False):
    # base case
    if (number == 0):
        return '' if track else '0'
    else:
        track = True
        rem = '1' if (number % 2 != 0) else '0'
        return findBinary(number//2, track) + rem


##### METHOD TWO ##########
def findBin(number, result):
    if number == 0:
        return result
    
    result = str(number % 2) + result
    return findBin(number // 2, result)


############ result testing #########
number = 23
if findBinary(number) == findBin(number, ''):
    print(findBinary(number))
else:
    print("NOT THE SAME OUTPUT")