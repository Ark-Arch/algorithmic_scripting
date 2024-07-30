def string_reversal(string, reversed_string=''):
    string_len = len(string)
    #base case
    if len(string) - 1 == 0:
        reversed_string += string[0]
        return (reversed_string)
    else:
        reversed_string += string[string_len - 1]
        return string_reversal(string[:len(string)-1], reversed_string)

string = 'important'
print(string_reversal(string))
