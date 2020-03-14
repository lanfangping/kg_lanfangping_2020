def char_map(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    if len(set1) >= len(set2):
        print('True')
    else: 
        print('False')
 


if __name__ == "__main__":
    str1 = input()
    str2 = input()
    char_map(str1, str2)