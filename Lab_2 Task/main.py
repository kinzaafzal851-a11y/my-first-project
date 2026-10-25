from course import Course, InvalidMarksError, load_course

# Task 1: Student test

print("Student Test")

c = Course("Programming for AI")

c.add_student("Ali", 88)
c.add_student("Zara", 92)
c.add_student("Omar", 75)

# Task 2: Course test

print("\nCourse Test")

print("Students:", len(c))
print("Average:", c.average())
print("Top student:", c.top_student())


# Exception test
print("\nException Test")

try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:", e)

print(c)

# Task 4: File test

print("\nFile Test")

c1 = load_course("Programming for AI", "marks.txt")

print(c1)
print("Top student:", c1.top_student())

# Wrong file test

print("\nWrong File Test")

load_course("Programming for AI", "mark.txt")

c = Course("X"); c.add_student("Ali",88)
c.remove_student("Ali")
print(len(c))
try:
    c.remove_student ("Zara")
except KeyError as e:
    print("KeyError:", e)