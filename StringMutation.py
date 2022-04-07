#You are given an immutable string, and you want to make changes to it.
def mutate_string(string, position, character):
    string_lis = list(string)    
    string_lis[position] = character
    string = ''.join(string_lis)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Another method
def mutate_string(string, position, character):
    string = string[:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
