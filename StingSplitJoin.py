#Program to replace spaces with '-' using built in string methods
def split_and_join(line):
    line_lis = line.split()
    return "-".join(line_lis)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#Pogram to replace spaces with '-' without using built in sting methods
def split_and_join(line):
    newstr=''
    for char in line:
        if(char == " "):
            char = '-'
        newstr += char
    
    return newstr

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
