
# Function to determine grade
def calculate_grade() :
# Input number of subjects
  n = int(input("Enter the number of subjects: "))
# Initialize total marks
  total_marks = 0
# Input marks for each subject
  for i in range (n):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total_marks += marks
# Calculate average marks
  average_marks = total_marks/n
# Determine grade
  if average_marks >= 90:
    grade = 'A'
  elif average_marks >= 75:
    grade = 'B'
  elif average_marks >= 60:
    grade = 'C'
  elif average_marks >= 50:
    grade = 'D'
  else:
    grade = 'F'
# Output result
  print (f"Average Marks: {average_marks}")
  print (f"Grade: {grade}")
# Call the function to calculate grade
calculate_grade ()