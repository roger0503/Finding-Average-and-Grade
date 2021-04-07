
marks = input("Enter the marks you got in each subject seperated by space: ")

marks_list = marks.split()

for i in range(len(marks_list)):
    marks_list[i] = int(marks_list[i])

average_marks = sum(marks_list)/len(marks_list)
print("Your avreage is:", average_marks)

def find_grade():
    if(average_marks >= 80):
        grade = 'A'
    elif(average_marks >= 60 and average_marks < 80):
        grade = 'B'
    elif(average_marks >= 50 and average_marks < 60):
        grade = 'C'
    else:
        grade = 'F'
    return grade

print("Your grade is:",find_grade())