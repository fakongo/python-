s='The working class'
print(s.startswith('Th'))
print(s.startswith('Th',5))
print(s.startswith('Th',0,5))

import os
[filename for filename in os.listdir(r'D:\\')
 if filename.endswith(('.bmp','.jdg','.gif'))]

print('12345abcd'.isalnum())
print('\t\n\r'.isspace())
print('aBC'.isupper())
print('12345abcd'.isalpha())
print('12345abcd'.isdigit())
print('1234.0'.isdecimal())
print('1234'.isdigit())

print('Main Menu'.center(20))
print('Main Menu'.center(20,'-'))
print('Main Menu'.ljust(20,'#'))
print('Main Menu'.rjust(20,'='))