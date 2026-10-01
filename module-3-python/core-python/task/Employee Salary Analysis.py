import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": [
        "Amit", "Bhavika", "Rahul", "Priya", "Neha",
        "Ravi", "Kiran", "Sneha", "Jay", "Pooja"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance", "HR",
        "Finance", "IT", "Finance", "HR", "IT"
    ],
    "Salary": [
        50000, 40000, 60000, 55000, 45000,
        65000, 70000, 50000, 48000, 62000
    ]
}

df = pd.DataFrame(data)
print(df)

# Department-wise average salary
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

#  Overall average salary
overall_avg = df["Salary"].mean()

print("Overall Average Salary:", overall_avg)

# Employees with salary above overall average
high_salary = df[df["Salary"] > overall_avg]
print(high_salary)

# bar chart
avg_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)

plt.show()