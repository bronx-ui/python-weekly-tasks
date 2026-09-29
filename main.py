from student import student_info

name = input("Enter student name: ")
age = input("Enter age: ")
course = input("Enter course: ")

print(student_info(name, age, course))

from temp import celsius_to_fahrenheit, fahrenheit_to_celsius

temperature = float(input("Enter temperature: "))
choice = input("Convert C to F or F to C? ")

if choice.upper() == "C":
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C = {result}°F")

elif choice.upper() == "F":
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F = {result}°C")

else:
    print("Invalid choice")

from grading import get_grade

name = input("Enter student name: ")
score = float(input("Enter score: "))

grade = get_grade(score)

print("Name:", name)
print("Score:", score)
print("Grade:", grade)