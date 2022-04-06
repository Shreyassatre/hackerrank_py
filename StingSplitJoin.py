def split_and_join(line):
    line_lis = line.split()
    return "-".join(line_lis)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
