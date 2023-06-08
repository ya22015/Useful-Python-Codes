# Install Pandas
pip install pandas

# Import libraries
from google.colab import files
import numpy as np
import pandas as pd

# Read input file
filename = input("Enter the input filename: ")
df = pd.read_csv(filename, header=None) # Read the input CSV file
n, cw = map(int, df.iloc[0, 0].split()) # Get the number of students and coursework weightage
df = df.iloc[1:n+1] # Extract only the rows containing student details
data = np.zeros((n, 4), dtype=np.int32) # Create an empty array to store the student data
for i in range(n):
    reg_no, exam, coursework = df.iloc[i, 0].split() # Get the registration number, exam and coursework marks for each student
    data[i][0] = int(reg_no) # Store the registration number in the array
    data[i][1] = round(float(exam)) # Store the rounded exam mark in the array
    data[i][2] = round(float(coursework)) # Store the rounded coursework mark in the array
    data[i][3] = round(0.6 * float(exam) + 0.4 * float(coursework)) # Calculate the overall mark and store in the array

# Define the data type for the array
dtype = np.dtype([('reg_no', np.int32), ('exam', np.int32), ('coursework', np.int32), ('overall', np.int32), ('grade', 'U2')])

# Convert the array to a list of tuples with grades and then convert it back to a structured array
grades = []
for row in data:
    overall_mark = row[3]
    if overall_mark < 40:
        grade = 'F'
    elif overall_mark < 50:
        grade = 'D'
    elif overall_mark < 60:
        grade = 'C'
    elif overall_mark < 70:
        grade = 'B'
    else:
        grade = 'A'
    grades.append((int(row[0]), int(row[1]), int(row[2]), int(row[3]), grade))
array2 = np.array(grades, dtype=dtype)

# Convert the array to a pandas DataFrame and sort by overall mark
df2 = pd.DataFrame(array2)
df2_sorted = df2.sort_values(by=['overall'], ascending=False)

# Print the sorted DataFrame
print(df2_sorted)

# Output results
first = second = third = fail = 0
failed_students = []
for i, row in df2.iterrows():
    if row['grade'] == 'A':
        first += 1
    elif row['grade'] == 'B':
        second += 1
    elif row['grade'] == 'C':
        third += 1
    else:
        fail += 1
        failed_students.append(str(int(row['reg_no'])))
print(f"Number of first class students: {first}") # Print the number of students who got first class
print(f"Number of second class students: {second}") # Print the number of students who got second class
print(f"Number of third class students: {third}") # Print the number of students who got third class
print(f"Number of failed students: {fail}") # Print the number of students who failed
print(f"Failed students: {', '.join(failed_students)}") # Print the registration numbers of the students who failed
