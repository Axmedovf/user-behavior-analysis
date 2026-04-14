import pandas as pd

data = pd.read_csv("users.csv")

filtered = data[data["age"] > 18]

filtered["category"] = filtered["spending"].apply(lambda x: "VIP" if x >= 1500 else ("Medium" if x >=800 else "Low"))

mean_spending = filtered["spending"].mean()
max_spending = filtered["spending"].max()

filtered = filtered.sort_values(by ="spending", ascending = False)

print(filtered)
print("Mean spending: ", mean_spending)
print("Max spending: ", max_spending)
filtered.to_csv("final_users.csv", index = False)
