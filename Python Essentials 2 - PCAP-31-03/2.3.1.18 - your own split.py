def mysplit(strng):
    string_list = []
    currstr = ""
    for ch in strng:
        if ch.isspace():
            if currstr != "":
                string_list.append(currstr)
                currstr = ""
        else:
            currstr = currstr + ch
            
    # Obtain the last piece of text before returning
    if currstr != "":
        string_list.append(currstr)
    
    return string_list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
