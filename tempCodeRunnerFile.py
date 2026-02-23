student_name = input("Enter the student name: ")

mark_01 = int(input("Enter the marked scored in physics(out of 100): "))
mark_02 = int(input("Enter the marked scored in Chemistry(out of 100): "))
mark_03 = int(input("Enter the marked scored in Biology(out of 100): "))
    
total_mark = mark_01 + mark_02 + mark_03
percentage = (total_mark / 300) * 100

print(student_name)
print(f"Total: {total_mark} / 300")
print(f"Percentage: {percentage}")

if percentage >= 75:
        print("Grade: A")
elif percentage >= 60:
        print("Grade: B")
elif percentage >= 40:
        print("Grade: C")
else:
        print("Grade: F")
