import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": [
        "Laptop", "Mobile", "Tablet", "Headphones",
        "Keyboard", "Mouse", "Monitor", "Printer"
    ],
    "Quantity": [
        45, 80, 35, 120,
        95, 150, 60, 40
    ]
}

df = pd.DataFrame(data)

print("Product Sales:")
print(df)

# Total quantity sold
total_quantity = df["Quantity"].sum()

print("\nTotal Quantity Sold:", total_quantity)

# Top 3 best-selling products
top_3 = df.sort_values("Quantity", ascending=False).head(3)

print("\nTop 3 Best-Selling Products:")
print(top_3)

# Pie chart
plt.pie(
    df["Quantity"],
    labels=df["Product"],
    autopct="%1.1f%%"
)

plt.title("Sales Distribution Among Products")
plt.show()
