#Program to find runner up score from given array/list 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    for i in range(-1, -n, -1):
        if(arr[i] == arr [i-1]):
            continue
        else:
            print(arr[i-1])
            break
