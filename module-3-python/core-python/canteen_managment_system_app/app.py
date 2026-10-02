# create a canteen management systems and evaluate by chart which food max westage 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data={
    "food":['pizza','burger','pasta','salad','sushi'],
    'salad':[10,5,2,8,1],
    'quantity':[100,200,150,80,50],
    'westage_food':[10,5,2,8,1]
}
df=pd.DataFrame(data)
print(df)
# find westage food
westage=df["westage_food"].max()
print("max westage food is:",westage)
# find food with maximum wastage
max_food=df.loc[df['westage_food'].idxmax(),'food']
print("\nmaximum wastage:",max_food)

plt.title('find westage food')
plt.pie(
    df['westage_food'],
    labels=df['food'],
    autopct='%1.1f%%',
    startangle=90
)
plt.show()