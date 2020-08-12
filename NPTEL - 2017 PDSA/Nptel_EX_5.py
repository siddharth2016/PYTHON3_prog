# NPTEL EXERCISE 5

courses = {}
students = []
grades = {}
f = 0
while(True):

    S = input()
    if S=="EndOfInput":
        break
    if S=='Courses':
        f = 1
        continue
    elif S=='Students':
        f = 2
        continue
    elif S=='Grades':
        f = 3
        continue

    if f==1 :
        S = S.split("~")
        courses[S[0]] = S[2:]
    elif f==2:
        S = S.split("~")
        students += [S]
    elif f==3:
        S = S.split("~")
        try:
            grades[S[0]].append(S[1:])
        except:
            grades[S[0]] = [S[1:]]
#print(courses)
#print(students)
#print(grades)
students.sort()
for stud in students:
    roll = stud[0]
    gpa = 0
    count = 0
    for key in grades.keys():
        for res in grades[key]:
            if roll==res[2]:
                count += 1
                if res[3]=='A':
                    gpa += 10
                elif res[3]=='AB':
                    gpa += 9
                elif res[3]=='B':
                    gpa += 8
                elif res[3]=='BC':
                    gpa += 7
                elif res[3]=='C':
                    gpa += 6
                elif res[3]=='CD':
                    gpa += 5
                elif res[3]=='D':
                    gpa += 4
    
    if gpa!=0:
        gpa = (gpa/count)
        ans = "~".join(stud) + "~" + "{0:3.1f}".format(gpa)
    else:
        ans = "~".join(stud) + "~" + str(gpa)
    print(ans)
