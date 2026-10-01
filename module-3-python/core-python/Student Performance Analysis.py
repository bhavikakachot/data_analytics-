import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": [
        "Amit", "Bhavika", "Rahul", "Priya", "Neha",
        "Ravi", "Kiran", "Sneha", "Jay", "Pooja"
    ],
    "Mathematics": [85, 92, 78, 88, 95, 72, 90, 84, 76, 91],
    "Science": [80, 95, 82, 85, 92, 75, 88, 86, 79, 94],
    "English": [88, 90, 80, 91, 89, 78, 85, 88, 82, 92]
}

df = pd.DataFrame(data)

# Calculate total marks
df["Total"] = df[["Mathematics", "Science", "English"]].sum(axis=1)

# Calculate average marks
df["Average"] = df[["Mathematics", "Science", "English"]].mean(axis=1)

print("Student Performance:")
print(df)

# Find student with highest average
highest_student = df.loc[df["Average"].idxmax()]

print("\nStudent with Highest Average:")
print(highest_student)

# Bar chart
plt.bar(df["Name"], df["Average"])

plt.title("Average Marks of Students")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)

plt.show()