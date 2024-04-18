def anagram_check(str1: str, str2: str) -> bool:
    str1_comp = str1.replace(' ','').upper()
    str2_comp = str2.replace(' ','').upper()

    if str1_comp != "":
        str1_list = list(str1_comp)
        str2_list = list(str2_comp)
        for i in range(len(str2_list)):
            letter_found = False
            for k in range(len(str1_list)):
                if str2_list[i] == str1_list[k]:
                    del str1_list[k]
                    letter_found = True
                    break
            if letter_found != True:
                return False
        
        return True
                
    else:
        return False


text1 = ""
while text1 == "":
    text1 = input("Enter a string: ")

text2 = ""
while text2 == "":
    text2 = input("Enter another string: ")

if anagram_check(text1, text2):
    print("Anagrams")
else:
    print("Not anagrams")