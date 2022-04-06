#in a dictonary name is key and each key has array of all subjects marks, find average marks of secified student name
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    lis=[]
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for names, scores in student_marks.items():
        if(names == query_name):
            lis = (student_marks[names])
            
    print('{:.2f}'.format(sum(lis)/len(lis)))
