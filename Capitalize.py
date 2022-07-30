def solve(s):
    result = ''
    
    L = s.split(" ")    
    for i in range(len(L)):
        result += L[i].capitalize()+' '
        
    return result
    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    
    
#Input:
#hello world

#Output:
#Hello World
