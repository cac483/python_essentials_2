def chars_in_string(input_chars: str, search_string: str) -> bool:
    if input_chars != "":
        for char in input_chars:
            pos_char = [pos for pos, c in enumerate(search_string) if char == c]
            if len(pos_char) == 0:
                return False
        return True
    else:
        return False


text1 = ""
while text1 == "":
    text1 = input("Enter characters to search: ")

text2 = ""
while text2 == "":
    text2 = input("Enter string to search in: ")

if chars_in_string(text1, text2):
    print("Yes")
else:
    print("No")