# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
var1 = n//2+1

for i in range(1, n*(n//2), 2):  
    print(('H'*i).center(n*(n//2),' '), end='\n')
    
for i in range(0, n+1):
    print(('H'*n).rjust(n+n//2,' '), end=' '*n*var1) 
    print(('H'*n).ljust(n+n//2,' '), end='\n') 
       
for i in range(0, n//2+1):
    print(('H'*n*n).rjust(n*n+n//2, ' '), end='\n')
    
for i in range(0, n+1):
    print(('H'*n).rjust(n+n//2,' '), end=' '*n*var1) 
    print(('H'*n).ljust(n+n//2,' '), end='\n') 
    
for i in range(n*(n//2)-1, 0, -2):  
    print(('H'*i).center(n*n*2,' '), end='\n')

# OUTPUT

#input is 5
    
#     H     
#    HHH    
#   HHHHH   
#  HHHHHHH  
# HHHHHHHHH 
#   HHHHH               HHHHH  
#   HHHHH               HHHHH  
#   HHHHH               HHHHH  
#   HHHHH               HHHHH  
#   HHHHH               HHHHH  
#   HHHHH               HHHHH  
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHHHHHHHHHHHHHHHHHHHHHH
#   HHHHH               HHHHH  
#   HHHHH               HHHHH  
#   HHHHH               HHHHH  
#   HHHHH               HHHHH  
#   HHHHH               HHHHH  
#   HHHHH               HHHHH  
#                     HHHHHHHHH                     
#                      HHHHHHH                      
#                       HHHHH                       
#                        HHH                        
#                         H
