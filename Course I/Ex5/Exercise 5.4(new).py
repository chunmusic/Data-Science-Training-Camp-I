# Exercise 5.3
import pandas as pd
pd.set_option('display.max_columns', 20)

fav_fruit = pd.read_table('fav_fruits.txt')

split_pattern = '[(\s+)(,\s+)]'

fav_split = fav_fruit['♥ Favourite Fruits ♥'].str.split(pat=split_pattern, expand=True)

fav_fruit = fav_split.drop(columns=[1, 3, 4, 5, 7, 9, 11, 16])

fav_fruit[6] = fav_fruit[6].replace('he','M')
fav_fruit[6] = fav_fruit[6].replace('she','F') 


fav_dummies = pd.get_dummies(fav_split)

fav_list = ['orange', 'apple', 'mango', 'cherry', 'peach', 'banana']

for fruit_name in fav_list:
  same_index_fruit = [colname for colname in fav_dummies.columns if fruit_name in colname]
  fav_fruit[fruit_name] = pd.concat([fav_dummies[same_index_fruit]]).sum(axis=1)


fav_fruit = fav_fruit.drop(columns= [8,10,12,13,14,15,17])


fav_fruit.rename(columns={0:'name'}, inplace=True)
fav_fruit.rename(columns={2:'age'}, inplace=True)
fav_fruit.rename(columns={6:'sex'}, inplace=True)


# Printing the final table
print("The number of apples is: " + str(fav_fruit['apple'].sum()))
print("The number of mango is: " + str(fav_fruit['mango'].sum()))
print("The number of cherry is: " + str(fav_fruit['cherry'].sum()))
print("The number of banana is: " + str(fav_fruit['banana'].sum()))
print("The number of orange is: " + str(fav_fruit['orange'].sum()))
print("The number of peach is: " + str(fav_fruit['peach'].sum()))