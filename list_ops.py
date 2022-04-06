#perform list operations which are given in input
if __name__ == '__main__':
    N = int(input())
    lis = []
    op = None
    
    for i in range(N): 
        op = (input().split())

        
        if(op[0] == 'insert'):
            lis.insert(int(op[1]), int(op[2]))
        elif(op[0] == 'print'):    
            print(lis)
        elif(op[0] == 'remove'):
            lis.remove(int(op[1]))
        elif(op[0] == 'sort'):
            lis.sort()
        elif(op[0] == 'pop'):
            lis.pop()
        elif(op[0] == 'append'):
            lis.append(int(op[1]))   
        elif(op[0] == 'reverse'):
            lis.reverse()  
        else:
            pass   
        
    
    
