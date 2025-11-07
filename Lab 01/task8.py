def get_grade(average):
  # Simulate switch-case using dictionary
  grade = {
      (90, 100): 'A+',
      (80, 89): 'A',
      (70, 79): 'B+',
      (60, 69): 'B',
      (50, 59): 'C+',
      (40, 49): 'C',
      (30, 39): 'D',
      (0, 29): 'F'
  }
  for range_tuple, grade_value in grade.items():
    if range_tuple[0] <= average <= range_tuple[1]:
      return grade_value
  return "Invalid Marks"

def main():
  n = int(input("Enter the number of subjects: "))
  total_marks = 0
  for i in range(n):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total_marks += marks
  average = total_marks / n
  print(f"The average marks are: {average}")
  grade = get_grade(average)
  print(f"The student's grade is: {grade}")

# Run the program
main()