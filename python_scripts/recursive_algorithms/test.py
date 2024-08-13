def test_function():
    return 'help'

a = 'always ' 
a += test_function()

b = a + test_function()

print(b)