import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": [
        "Day 1", "Day 2", "Day 3", "Day 4", "Day 5",
        "Day 6", "Day 7", "Day 8", "Day 9", "Day 10",
        "Day 11", "Day 12", "Day 13", "Day 14", "Day 15"
    ],
    "Temperature": [
        28, 30, 27, 32, 35,
        31, 29, 33, 36, 34,
        30, 37, 35, 32, 38
    ]
}

df = pd.DataFrame(data)

print("Temperature Data:")
print(df)

# Maximum temperature
max_temp = df["Temperature"].max()
print("\nMaximum Temperature:", max_temp)

# Minimum temperature
min_temp = df["Temperature"].min()
print("Minimum Temperature:", min_temp)

# Average temperature
avg_temp = df["Temperature"].mean()
print("Average Temperature:", avg_temp)

# Days where temperature is above average
above_average = df[df["Temperature"] > avg_temp]

print("\nDays Above Average Temperature:")
print(above_average)

# Line plot
plt.plot(df["Day"], df["Temperature"], marker="o")

plt.title("Temperature Variation Over 15 Days")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

plt.show()