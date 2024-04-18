def read_int(prompt, min, max):
    num = input(prompt)
    try:
        assert float(num) <= 10 and float(num) >= -10
        return num
    except ValueError:
        print("Error: wrong input")
        raise
    except AssertionError:
        print("Error: the value is not within permitted range (-10..10)")
        raise


try:
    v = read_int("Enter a number from -10 to 10: ", -10, 10)
    print("The number is:", v)
except (ValueError, AssertionError):
    print("Error occurred.")