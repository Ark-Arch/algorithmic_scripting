def sumNaturalNumber(number):
    if number < 2:
        return number
    else:
        return number + sumNaturalNumber(number -1)

## OPTIMISED CODE
def sumNaturalNumbers(number):
    return ((number*(number+1))/2)


number = 10
if sumNaturalNumber(number) == sumNaturalNumbers(number):
    print(sumNaturalNumber(number))
else:
    print('NOT THE SAME OUTPUT')