import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ],
    "Sales": [
        45000, 52000, 48000, 60000,
        55000, 65000, 70000, 68000,
        58000, 75000, 80000, 90000
    ]
}

df = pd.DataFrame(data)

print("Monthly Sales:")
print(df)

# Total annual sales
total_sales = df["Sales"].sum()

print("\nTotal Annual Sales:", total_sales)

# Month with highest sales
highest_month = df.loc[df["Sales"].idxmax()]

print("\nMonth with Highest Sales:")
print(highest_month)

# Month with lowest sales
lowest_month = df.loc[df["Sales"].idxmin()]

print("\nMonth with Lowest Sales:")
print(lowest_month)

# Line plot
plt.plot(df["Month"], df["Sales"], marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.show()