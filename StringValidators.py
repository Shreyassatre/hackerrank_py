# find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
if __name__ == '__main__':
    s = input()
    up_case = ''
    low_case = '' 
    digit = ''
    symbol = ''
    
    if(up_case == '' or low_case == '' or digit == ''):
        for char in s:
            if(char.isupper()):
                up_case += char
            if(char.islower()):
                low_case += char
            if(char.isdigit()):
                digit += char
        
    if(up_case != '' or low_case != '' or digit != ''):
        print(True)
    else:
        print(False)
        
    if(up_case != '' or low_case != ''):
        print(True)
    else:
        print(False)
        
    if(digit != ''):
        print(True)
    else:
        print(False)
        
    if(low_case != ''):
        print(True)
    else:
        print(False)
                
    if(up_case != ''):
        print(True)
    else:
        print(False)
