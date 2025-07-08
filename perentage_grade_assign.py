print(" Enter your marks for 3 subjects:\n")


marks1 = float(input("Subject 1: "))
marks2 = float(input("Subject 2: "))
marks3 = float(input("Subject 3: "))

obtain = marks1 + marks2 + marks3
total = 500
percentage = (obtain / total) * 100  

if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"


print(" --- Result ---")
print(f"Total Marks: {obtain}/{total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

