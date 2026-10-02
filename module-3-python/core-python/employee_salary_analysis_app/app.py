# used all libraries
import pandas as pd
import matplotlib.pyplot as plt
# create a data
data={
    "name":["Alice","Bob","Charlie","David","Eva"],
    "age":[25,30,35,40,45],
    "salary":[50000,60000,70000,80000,90000]
    }

# create a DataFrame or tabular data
df=pd.DataFrame(data)
print(df)

# create a total salary column
print("----------------------------------")
df['total_salary']=df['salary'].sum()
print("total salary:",df['total_salary'])

# avarage salary
print("----------------------------------")
df['average_salary']=df['salary'].mean()
print("average salary:",df['average_salary'])

# create a tabular data for age and salary
print("----------------------------------")
age_salary_df=df[['age','salary']]
print(age_salary_df)


# create a bar chart for employee name who get > salary then average salary
print("----------------------------------")
high_erners=df[df['salary']>df['average_salary']]
print(high_erners)

# display data of high erners in bar chart
#plt.title("high erners")
#plt.bar(high_erners['name'],high_erners['salary'],color='coral')
#plt.xlabel("name")
#plt.ylabel("salary")
#plt.show()

# display data in line chart 
plt.title("high_erners")
plt.plot(high_erners['name'],high_erners['salary'],color='coral',marker='o')
plt.xlabel("name")
plt.ylabel("salary")
plt.show()