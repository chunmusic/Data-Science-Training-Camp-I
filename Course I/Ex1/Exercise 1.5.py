# Exercise 1.5

# No. 1
import pandas as pd

df = pd.read_csv("cities.csv")

print(df[:100])

# No. 2
print("No.2")
df = df.drop("NS", 1)
df = df.drop("EW", 1)

print(df)




# No. 3

print("No.3")

rep = pd.read_csv("representative.csv")

df = pd.DataFrame.join(rep[["Name","Height(inches)","Weight(lbs)"]], df)


print(df)




# No. 4
print("No.4")
df = df.drop(df.index[[91]])
df = df.drop(df.index[[98]])

print(df)



# No. 5

print("No.5")

df = df[df.State != "CA"]

print(df)


# No. 6


df.to_csv('cities_no_CA.csv', index = False, header=True)