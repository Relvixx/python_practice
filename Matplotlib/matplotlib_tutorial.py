import matplotlib.pyplot as plt
import pandas as pd

"""x = [4,5,6]
y = [1,2,3]

plt.plot(x,y)
plt.grid()
plt.show()"""

data = {
    "salery": [30000, 37000, 42000, 46000, 54000, 59000, 61000, 63000, 70000, 77000, 80000, 87000, 92000, 66000, 74000, 89000, 64000, 66000, 75000, 73000]
}

df = pd.DataFrame(data)
print(df.head())

df["dept"] = ["HR", "IT", "Finance","HR", "IT", "Finance","HR", "IT", "Finance","HR", ] * 2
print(df.head(21))

"""print(df.shape)
plt.plot(df["salery"], color = "red", marker = "o")   # plot the salary column
plt.grid()
plt.show()

plt.hist(df["salery"])   # plot the salary column
plt.show()"""

count = df["dept"].value_counts()

plt.pie(count, labels=count.index, autopct= "%1.1f", explode=[0.2, 0.1, 0.3])
plt.show()
