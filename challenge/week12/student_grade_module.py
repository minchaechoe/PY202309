import Student as sc

# Read data and create instances of the Student class
lines = open("students.csv", "r", encoding="utf8").readlines()
lines = lines[1:] # slicing for excepting index

students_info = dict()
for line in lines:
    arr = line.strip().split(",")
    name = arr[0]
    korean_score = arr[1]
    math_score = arr[2]
    english_score = arr[3]
    students_info[name] = sc.Student(name, korean_score, math_score, english_score)

# Calculate and print average scores
students_ins = list(students_info.values())

for student in students_ins:
    print(f"{student.name}의 평균 점수는 {student.get_average()}")

# Write average.txt file
with open("./average.txt", "w", encoding="utf8") as writer_fp:
    writer_fp.write("-----학생들의 평균 점수-----\n")
    for student in students_ins:
        writer_fp.write(f"{student.name}의 평균 점수는 {student.get_average()}\n")