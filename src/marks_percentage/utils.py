#In this problem we are taking input of marks of students
#In the Result We are getting the average of marks of desired student
#I have also considered incase any error happens we will get a error message

import logging
logging.basicConfig(level=logging.INFO,format='%(message)s')
def read_student_marks():
    n = int(input().strip())
    student_marks = {}
    for _ in range(n):
        name, *line = input().strip().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    return student_marks

def calculate_average_marks(student_marks, query_name):
    if query_name in student_marks:
        avg_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
        return avg_marks
    else:
        logging.error("Student name not found in records")
def average_marks():
    student_marks = read_student_marks()
    query_name = input().strip()
    avg_marks = calculate_average_marks(student_marks, query_name)
    if avg_marks:
        logging.info(f"{avg_marks:.2f}")
    else:
        logging.error("Failed to calculate average marks")
