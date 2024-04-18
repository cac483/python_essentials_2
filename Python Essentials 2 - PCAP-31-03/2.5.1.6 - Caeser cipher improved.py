def caesar_cipher(input_str: str, shift: int) -> str:
    return_val = ""
    ord_val = 0
    for char in input_str:
        if char.isalpha():
            ord_val = ord(char)
            if char.isupper():
                ord_val = (((ord_val - ord('A')) + shift) % 26) + ord('A')
            else:
                ord_val = (((ord_val - ord('a')) + shift) % 26) + ord('a')
            return_val = return_val + chr(ord_val)
        else:
            return_val = return_val + char
    
    return return_val


shift_val = ""
text = ""

while text == "":
    text = input("Enter some text to encrypt: ")

while shift_val == "":
    try:
        shift_val = input("Enter the cipher shift value (default: 2): ")
        if shift_val == "":
            shift_val = "2"
        shift_val_int = abs(int(shift_val))
        if shift_val_int > 25:
            print("Shift value too large.  Please re-enter.")
            shift_val = ""
    except ValueError:
        print("Incorrect shift value. Please re-enter.")
        print()
        shift_val = ""

print(caesar_cipher(text, shift_val_int))
