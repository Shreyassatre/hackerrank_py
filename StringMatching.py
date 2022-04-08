#Print the number of times that the substring occurs in the given string.
def count_substring(string, sub_string):
    pos= []
    count = 0
    
    for i in range(len(string)):
        if(sub_string[0] == string[i]):
            pos.append(i)
            
    for i in range(len(pos)):
        if(string[pos[i]:pos[i]+len(sub_string)] == sub_string):
            count += 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
