import logging

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