#Print a list of all possible coordinates given by(i,j,k)on a 3D grid where the sum i+j+k of  is not equal to n.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    res = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print (res)
