# Exercise 1.2
# No. 1
import pandas as pd

age = pd.read_csv("oscar_age_female.csv")
age_data = age['Age'] 

print(age_data)

# No. 2

data = pd.read_csv("oscar_age_female.csv")
actress_age = data['Age'] 
avg = sum(actress_age)/len(actress_age)

print(avg)

# No. 3

data_semi = pd.read_csv("username.csv", sep=';')
print(data_semi)


# No. 4
print("")

data_html = pd.read_html("time_table.html")
print(data_html)
