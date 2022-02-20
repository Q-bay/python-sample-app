import sys
import math

def main():
    print('start!' )
    target_str = input()
    reverse_str(target_str)
    print('end!' )

def reverse_str(target_str):
    len_str = len(target_str)
    return_str = ''
    i = -1
    while -len_str <= i:
        return_str = return_str + target_str[i]
        i = i -1
    print(return_str)



if __name__ == "__main__":
    main()
