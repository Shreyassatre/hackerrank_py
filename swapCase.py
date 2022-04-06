#swap cases of given sting, i.e convert uppercase letter to lowercase and lowercase to uppercase without using built in string method(swapcase())
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
    
    
#simple code in python to swap cases of sting using built in method

def swap_case(s):
    res = s.swapcase()
    
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
