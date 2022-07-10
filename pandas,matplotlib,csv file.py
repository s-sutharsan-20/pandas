import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\User\\OneDrive\\Desktop\\python programs2\\kohli.csv")
plt.plot(df.year,df.runs)
plt.title("Virat Kohli's Test Runs ")
plt.xlabel("Year")
plt.ylabel("Runs")
plt.show()
