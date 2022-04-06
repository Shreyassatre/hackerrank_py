#in 2 dimentional array the students name and scores are given, find second lowest score, if more than 1 student having same second lowest score then print their names in alphabetical order
if __name__ == '__main__':
    students = []
    newlis = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        details = [name, score]
        students.append(details)
    
    students.sort(key=lambda x:x[1])

    for i in range(1,len(students)):
        if(students[i-1][1] == students[i][1]):
            continue
        newlis.append(students[i])
        break
    
    for j in range(i+1, len(students)):
        if(students[j-1][1] == students[j][1]):
            newlis.append(students[j])
        else:
            break
    
    newlis.sort(key = lambda x:x[0])
    
    for k in range(0, len(newlis)):
        print(newlis[k][0])
        
