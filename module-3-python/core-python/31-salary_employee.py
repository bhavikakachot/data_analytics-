# thierd party module
# third party module is installable
# pip install modulename
# python -m pip install modulename

# pandas
# numpy
# matplotlib
# seaborn
# request

import pandas as pd
import matplotlib.pyplot as plt
data={
    "name":["a","b","c","d","e"],
    "salary":[20000,21000,23000,34000,30000]

}
# print using pandas
df=pd.DataFrame(data)
print(df)

# create title
plt.title("employee name and salary")
plt.xlabel("name")
plt.ylabel("salary")
plt.bar(df["name"],df["salary"])
# sum of salary of employee
print('-----------sum of salary-------------')
print("sum of salary :",df["salary"].sum())
# pi chart
# plt.pie(df["salary"],labels=df["name"],autopct="%1.1f%%")
# disply matplotlib data
plt.show()