def is_palindrome(string):
    string = string.replace(" ", "").lower()
    if string == string[::-1]:
        return True
    else:
        return False
input_string = "А роза упала на лапу Азора"
print(is_palindrome(input_string))


