def display_seven_segment(num):
    try:
        float_num = float(num)
    except ValueError:
        return
    except TypeError:
        return
    
    str_num = str(float_num)
    
    str_lines = ["", "", "", "", ""]
    
    for chr in str_num:
        match chr:
            case '0':
                str_lines[0] += " ***"
                str_lines[1] += " * *"
                str_lines[2] += " * *"
                str_lines[3] += " * *"
                str_lines[4] += " ***"
            case '1':
                str_lines[0] += "   *"
                str_lines[1] += "   *"
                str_lines[2] += "   *"
                str_lines[3] += "   *"
                str_lines[4] += "   *"
            case '2':
                str_lines[0] += " ***"
                str_lines[1] += "   *"
                str_lines[2] += " ***"
                str_lines[3] += " *  "
                str_lines[4] += " ***"
            case '3':
                str_lines[0] += " ***"
                str_lines[1] += "   *"
                str_lines[2] += " ***"
                str_lines[3] += "   *"
                str_lines[4] += " ***"
            case '4':
                str_lines[0] += " * *"
                str_lines[1] += " * *"
                str_lines[2] += " ***"
                str_lines[3] += "   *"
                str_lines[4] += "   *"
            case '5':
                str_lines[0] += " ***"
                str_lines[1] += " *  "
                str_lines[2] += " ***"
                str_lines[3] += "   *"
                str_lines[4] += " ***"
            case '6':
                str_lines[0] += " ***"
                str_lines[1] += " *  "
                str_lines[2] += " ***"
                str_lines[3] += " * *"
                str_lines[4] += " ***"
            case '7':
                str_lines[0] += " ***"
                str_lines[1] += "   *"
                str_lines[2] += "   *"
                str_lines[3] += "   *"
                str_lines[4] += "   *"
            case '8':
                str_lines[0] += " ***"
                str_lines[1] += " * *"
                str_lines[2] += " ***"
                str_lines[3] += " * *"
                str_lines[4] += " ***"
            case '9':
                str_lines[0] += " ***"
                str_lines[1] += " * *"
                str_lines[2] += " ***"
                str_lines[3] += "   *"
                str_lines[4] += " ***"
            case '-':
                str_lines[0] += "    "
                str_lines[1] += "    "
                str_lines[2] += " ***"
                str_lines[3] += "    "
                str_lines[4] += "    "
            case '.':
                str_lines[0] += "    "
                str_lines[1] += "    "
                str_lines[2] += "    "
                str_lines[3] += "    "
                str_lines[4] += "  * "

    for i in range(5):
        print(str_lines[i])

display_seven_segment(3.141592653)