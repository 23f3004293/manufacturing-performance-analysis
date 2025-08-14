# analysis.py
# Author: 23f3004293@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

# Quarterly efficiency data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Efficiency": [73.35, 73.28, 77.47, 82.07]
}

industry_target = 90

# Create DataFrame
df = pd.DataFrame(data)

# Calculate average efficiency
average_efficiency = df["Efficiency"].mean()
print(f"Average efficiency: {average_efficiency:.2f}")

# Plot trend and benchmark
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["Efficiency"], marker="o", label="Equipment Efficiency")
plt.axhline(industry_target, color="red", linestyle="--", label="Industry Target")
plt.title("Quarterly Equipment Efficiency Rate (2024)")
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate")
plt.ylim(70, 95)
plt.legend()
plt.grid(True)
plt.savefig("efficiency_trend.png")
plt.close()
