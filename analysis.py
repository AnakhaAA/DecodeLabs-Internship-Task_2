import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("Dataset for Data Analytics (1).xlsx")
print(data.head())
print(data.info())
print(data.describe())
print("Total Sales:",
      data["TotalPrice"].sum())


print("Average Order:",
      data["TotalPrice"].mean())


print(data["Product"].value_counts())


data["Product"].value_counts().plot(kind="bar")

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Orders")

plt.show()


print("Highest Orders:")

print(data["TotalPrice"]
      .sort_values(ascending=False)
      .head())