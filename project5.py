import pandas as pd

data = pd.read_csv("users.csv")

filtered = data[data["age"] > 18]

filtered["category"] = filtered["spending"].apply(lambda x: "VIP" if x >= 1500 else ("Medium" if x >=800 else "Low"))

mean_spending = filtered["spending"].mean()
max_spending = filtered["spending"].max()

category_count = filtered["category"].value_counts()
category_percent = filtered["category"].value_counts(normalize=True) * 100

filtered = filtered.sort_values(by ="spending", ascending = False)

print(filtered)
print("Mean spending: ", mean_spending)
print("Max spending: ", max_spending)
print("\nUsers by category")
print(category_count)
print("\nCategory percentage: ")
print(category_percent.round(2).astype(str) + "%")
filtered.to_csv("final_users.csv", index = False)
category_count.to_csv("category_summary.csv", header = ["count"])
category_percent.to_csv("category_percentage.csv",header = ["percentage (%)"])
