# create a attendance managment system
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# create a student attendance data
data={
    "studentname":["a","b","c","d","e","f"],
    "total_days":[100,100,100,100,100,100],
    "absent_days":[30,20,40,10,5,45]
}
# print data
# calculate in tabular layout
df=pd.DataFrame(data)
print(df)

# total attendance days
print("------------------------------")
total_days=df["total_days"].sum()
print("total attendance days is:",total_days)

# total absent days
print("------------------------------")
total_absent_days=df["absent_days"].sum()
print("total absent days is:",total_absent_days)

# maximum absent student 
print("------------------------------")
maximum_absent_day=df["absent_days"].max()
print("maximum_absent_days:",maximum_absent_day)

# maximum absent student who is max absent
print("------------------------------")
maximum_absent_student=df.loc[df["absent_days"].idxmax(),"studentname"]
print("maximum_absent student is:",maximum_absent_student)

# data visualised using matplotlib in chart
plt.title("maximum absent student data visualized")
plt.pie(
    df["absent_days"],
    labels=df["studentname"],
    colors=["yellow","green","pink","blue","gray","red"],
    autopct="%1.1f%%"
)
# generate data in excel
df.to_excel("students_data.xlsx",engine="openpyxl",index="False")
print("data generated in excel succesfully")
plt.show()