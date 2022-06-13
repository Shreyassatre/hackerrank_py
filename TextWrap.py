#with textwrap
import textwrap

def wrap(string, max_width):
    return ('\n'.join(textwrap.wrap(string, max_width)))
  
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
    
#Wihotut Text Wrap
i=0
def wrap(string, max_width):
    return ('\n'.join(string[i:i+max_width] for i in range(0, len(string), max_width)))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
    
    
# input
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Output
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
    
