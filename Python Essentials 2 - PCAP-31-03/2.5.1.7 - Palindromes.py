def palindrome(input_str: str) -> bool:
    compare_str = input_str.replace(' ', '').replace('.', '').replace(',', '').upper()
    if len(compare_str) > 0:
        result = True
        for i in range(len(compare_str)):
            if compare_str[i] != compare_str[len(compare_str) - 1 - i]:
                result = False
        return result
    else:
        return False

text = ""
while text == "":
    text = input("Enter some text: ")

if palindrome(text):
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")