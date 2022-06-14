#designed a new door mat with the following specifications: Mat size must be N X M. (N is an odd natural number, and M is 3 times .), The design should have 'WELCOME' written in the center. ,The design pattern should only use |, . and - characters.

if __name__ == '__main__':
    n,m = map(int, input().split(' '))
    
    for i in range(1,n,2):
        print(('.|.'*i).center(m,'-'))
    
    print('WELCOME'.center(m,'-'))
    
    for i in range(n-2,0,-2):
        print(('.|.'*i).center(m,'-'))
        
        
# input:
# 7 21

# Output:
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
