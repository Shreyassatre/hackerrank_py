#The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.

def print_formatted(n):  
    padd = len(str(bin(n)))-2
        
    for i in range(1,n+1):
        dec = str(i)
        octal = str(oct(i))
        hexa = str(hex(i)).upper()
        bina = str(bin(i))
        
        print(dec.rjust(padd),octal[2:].rjust(padd),hexa[2:].rjust(padd),bina[2:].rjust(padd))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

 

#Another Method

def print_formatted(n):  
    width = len(str(bin(n)))-2
        
    for i in range(1,n+1):
        for base in('d','o','X','b'):
            print('{0:{width}{base}}'.format(i, base=base, width=width),end=' ')
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
