import sys

def char_map(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    if len(set1) >= len(set2):
        print('True')
    else: 
        print('False')
 


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Invalid Input")
    else:
        str1 = sys.argv[1]
        str2 = sys.argv[2]
        char_map(str1, str2)