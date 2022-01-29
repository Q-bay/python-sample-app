from distutils import extension
import sys
import re
import os

path = ''
file_name = ''
file_extension = ''
number_of_creations = ''

def main():
    
    if not path_config():
        print('specify valid path.') 
        exit()

    if not check_config():
        exit()

    

def path_config():
    print('specify path to create files.')
    path = input()
    if os.path.exists(path):
        return True
    return False

def file_config():
    
    print('specify file name.')
    file_name = input()
    
    print('specify file extension.')
    file_extension = input()

    number_of_creations = number_of_creations_config()

def check_config():
    print('check your configuration.')
    print('path:{0}'.format(path))
    print('file name:{0}'.format(file_name))
    print('file file extension:{0}'.format(file_extension))
    print('file number of creations:{0}'.format(number_of_creations))
    print('1:OK')
    print('2:RECONFIG')
    print('3:CREATE CANCEL')
    select_type = input()
    
    if not select_type.isdigit():
        print('specify number.')
        check_config()
    
    if select_type == 1:
        return True
    if select_type == 2:
        check_config()
    if select_type == 3:
        return False
    print('specify number 1 ~ 3.')
    check_config()

def number_of_creations_config():
    print('specify file number_of_creations.')
    number_of_creations = input()
    if not number_of_creations:
        print('specify number.')
        number_of_creations_config()
    return number_of_creations

if __name__ == "__main__":
    main()