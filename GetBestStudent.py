'''
Created on 14-Oct-2020

@author: AA20090212 - AAYUSH KUMAR SRIVASTAVA
'''
def get_best_student(studentMarks):
    avgMarks = 0;
    name = ''
    for student in studentMarks:
        stu_avg_marks = sum(studentMarks[student])/len(studentMarks[student])
        if avgMarks < stu_avg_marks:
            avgMarks = stu_avg_marks
            name = student
    return name


if __name__ == '__main__':
    print(get_best_student({
  "Avisek": [100, 90, 80],
  "Anand": [100, 70, 80],
  "Aayush": [100, 90, 90]
}))