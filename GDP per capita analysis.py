import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("gdp_per_capita.csv")
print(df.head())

plt.figure(figsize = (10,8))

#GDP
plt.subplot(5,1,1)
plt.plot(df["Years"], df["Japan"], label = "Japan")
plt.plot(df["Years"], df["Philippines"], label = "Philippines")
#Rolling Average
df["Japan MA"] = df["Japan"].rolling(5).mean()
df["Philippines MA"] = df["Philippines"].rolling(5).mean()
plt.plot(df["Years"], df["Japan MA"], linestyle = "--", label = "Japan MA (5 yrs)")
plt.plot(df["Years"], df["Philippines MA"], linestyle = "--", label = "Philippines MA (5 yrs)")
plt.xlabel("Years")
plt.ylabel("GDP per Capita ($)")
plt.title("GDP per Capita Comparison: Japan vs Philippines")
plt.legend()
plt.grid()

#Difference
plt.subplot(5,1,2)
df["Difference"] = df["Japan"] - df["Philippines"]
plt.plot(df["Years"], df["Difference"], label = "GDP per Capita Gap")
plt.xlabel("Years")
plt.ylabel("Gap ($)")
plt.title("GDP per Capita Gap: Japan - Philippines")
plt.legend()
plt.grid()

#Growth rate
plt.subplot(5,1,3)
df["Japan Growth"] = df["Japan"].pct_change()
df["Philippines Growth"] = df["Philippines"].pct_change()
plt.plot(df["Years"], df["Japan Growth"], label = "Japan Growth")
plt.plot(df["Years"], df["Philippines Growth"], label = "Philippines Growth")
plt.xlabel("Years")
plt.ylabel("Growth Rate($)")
plt.title("GDP per Capita Growth Rate")
plt.legend()
plt.grid()

#Ratio
plt.subplot(5,1,4)
df["Ratio"] = df["Philippines"] / df["Japan"]
plt.plot(df["Years"], df["Ratio"], label = "Ratio")
#Ratio Rolling Average
df["Ratio MA"] = df["Ratio"].rolling(5).mean()
plt.plot(df["Years"], df["Ratio MA"], linestyle = "--", label = "Ratio MA (5yrs)")
plt.xlabel("Years")
plt.ylabel("Ratio")
plt.title("GDP per Capita Ratio")
plt.legend()
plt.grid()

#Scatter Diagram
plt.subplot(5,1,5)
plt.scatter(df["Japan"], df["Philippines"])
#Regression Line
m, b = np.polyfit(df["Japan"], df["Philippines"], 1)
plt.plot(df["Japan"], m*df["Japan"] + b)
plt.text(df["Japan"].min(), df["Philippines"].max(), f"Slope: {m:.3f}")
#Correlation
correlation = np.corrcoef(df["Japan"], df["Philippines"]) [0,1]
print(f"correlation: {correlation: .3f}")
plt.text(df["Japan"].min(), df["Philippines"].max()*0.9, f"Corr: {correlation:.3f}")
plt.xlabel("Japan GDP per Capita")
plt.ylabel("Philippines GDP per Capita")
plt.title("Relationship Between Japan and Philippines GDP per Capita")
plt.grid()

plt.tight_layout()
plt.savefig("gdp_per_capita_analysis.png")
plt.show()

#Title: GDP per Capita Comparison Analysis: Japan vs Philippines (World Bank Data)
#Using real-world data from the World Bank, Japan has significantly higher GDP per capita than the Philippines throughout the years observed.
#However, the Philippines tends to have more consistent growth, while Japan shows more fluctuations during economic downturns.
#The GDP per capita gap grown rapidly from the 1960s to 1990s due to Japan's rapid economic development.
#The scatter plot shows a positive relationship between Japan and the Philippines' GDP per capita.
#The regression line indicates that as Japan's GDP per capita increases, the Philippines' GDP per capita also tends to increase.
#The correlation coefficient of 0.736 suggests a strong positive relationship between the two economies.


