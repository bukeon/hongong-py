input_data = input("")
list_a = list(input_data)
list_b = list(reversed(list_a))

def is_palindrome(input_data):

    if list_a==list_b :
        return "palindrome"
    else :
        return "not palindrome"
    


# TODO: 입력 데이터를 input_data에 저장하고, is_palindrome 함수를 구현하세요.
print(f'{is_palindrome(input_data)}')