def digit_of_life(str_digits: str) -> str:
    total = 0
    for char in str_digits:
        try:
            value = int(char)
        except ValueError:
            value = 0
        
        total += value
        if total > 9:
            total -= 9
    
    return str(total)


text = ""
while text == "":
    text = input("Enter your birthday in the YYYYMMDD format: ")

print(digit_of_life(text))