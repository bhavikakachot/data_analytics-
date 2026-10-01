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
    "age":[20,21,23,34,30]

}
# print using pandas
df=pd.DataFrame(data)
print(df)

# create title
plt.title("employee name and age")
plt.xlabel("name")
plt.ylabel("age")
plt.bar(df["name"],df["age"])
# pi chart
# plt.pie(df["age"],labels=df["name"],autopct="%1.1f%%")
# disply matplotlib data
plt.show()