import sys
import re

def convert_charctor_camel_to_snake(charactor):
    converted_charactor = ''

    for char in charactor:
        if re.match(r'[A-Z]', char):
            char = '_' + char.lower()
        converted_charactor += char
    return converted_charactor

def convert_charctor_snake_to_camel(charactor):
    converted_charactor = ''
    under_score_flag = False

    for char in charactor:
        if char == '_':
            under_score_flag = True
            continue

        if under_score_flag == True:
            converted_charactor += char.upper()
            under_score_flag = False
            continue

        converted_charactor += char

    return converted_charactor


print('choose this convert type.' )
print('1: convert camel to snake.' )
print('2: convert snake to camel.' )

convert_type = input()

if convert_type not in ('1', '2'):
    print('convert type must be 1 or 2 !')
    exit()

print('specify charactor string.')
charactor = input()

if convert_type == '1':
    print(convert_charctor_camel_to_snake(charactor))
elif convert_type == '2':
    print(convert_charctor_snake_to_camel(charactor))