def string_reversal(string, reversed_string = ''):
    # base case
    if len(string) == 0:
        return reversed_string
    else:
        reversed_string += string.pop() #O(1)
        return string_reversal(string, reversed_string)

string = list('important')
answer = string_reversal(string)

print(answer)