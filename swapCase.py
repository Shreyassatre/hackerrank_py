def swap_case(s):
    substr = ''
    res = ''
    for char in s:
        ascival = ord(char)
        
        if(ascival in range(65,90+1)):
            res += char.lower()
        elif(ascival in range(97, 122+1)):
            res += char.upper()
        else:
            res += char
    
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    
#or simple code in python is

def swap_case(s):
    res = s.swapcase()
    
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)