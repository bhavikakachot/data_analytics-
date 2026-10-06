import pandas as pd
import matplotlib.pyplot as plt
data={
    "name":["a","b","c","d","e","f","g","h","j","k"],
    "attendance":[0,0,1,1,1,0,1,1,1,0]

}
# crate a pie chart
df=pd.DataFrame(data)
print(df)

# find absent and present 
present=(df["attendance"]==1).sum()
absent=(df["attendance"]==0).sum()
colors=["green","red"]
values=[present,absent]
lables=["present","absent"]
print("total present student s list is :",present)
print("total absent student s list is :",absent)

# find the dynamic details in list in graph or chart
plt.title("student attendance managment system")
plt.pie(values,
        labels=lables,
        colors=["green","red"],
        autopct="%1.1f%%"
        )
plt.show()
