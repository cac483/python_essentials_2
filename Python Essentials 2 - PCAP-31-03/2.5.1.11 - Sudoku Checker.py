# Read in input
input = [
    "295743861",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "154938672"
]
result = True

# Analyze each line for 1 - 9
for line in input:
    sum = 0
    for chr in line:
        try:
            if int(chr) > 0:
                sum += int(chr)
            else:
                result = False
        except Exception:
            result = False
    if sum != 45:
        result = False

# Analyze each column for 1 - 9
for i in range(9):
    sum = 0
    for k in range(9):
        try:
            if int(input[i][k]) > 0:
                sum += int(input[i][k])
            else:
                result = False
        except Exception:
            result = False


# Analyze each 3x3 block for 1 - 9
for c in range(0,9,3):
    for r in range(0,9,3):
        sum = 0
        try:
            for a in range(3):
                sum += int(input[c + a][r]) + int(input[c + a][r + 1]) + int(input[c + a][r + 2])
        except Exception:
            result = False
        if sum != 45:
            result = False

# Return result
if result:
    print("Yes")
else:
    print("No")