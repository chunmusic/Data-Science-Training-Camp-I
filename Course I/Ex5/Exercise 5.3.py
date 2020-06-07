# Exercise 5.3
import pandas as pd
pd.set_option('display.max_columns', 20)

# Reading the txt file (no header). This will give data with 1 column.
fav_fruit = pd.read_table('fav_fruits.txt')

# Splitting that column word by word. Use the pattern provided.
split_pattern = '[(\s+)(,\s+)]'

fav_split = fav_fruit['♥ Favourite Fruits ♥'].str.split(pat=split_pattern, expand=True)

# Dropping unnecessary columns

fav_fruit = fav_split.drop(columns=[1, 3, 4, 5, 7, 9, 11, 16])


# Replacing ['he','she'] with ['M','F']. Use pd.replace().
fav_fruit[6] = fav_fruit[6].replace('he','M')
fav_fruit[6] = fav_fruit[6].replace('she','F') 

# Converting columns containing fruit names into dummy variable

fav_dummies = pd.get_dummies(fav_split)

# Reading txt file containing fruits list
fruit_list = pd.read_csv('fruit_list.txt', squeeze=True) # squeeze so it can be used in for loop


# Combining columns consisting of dummy variable with same name

for fruit_name in fruit_list:
  # Making a list of header in course_dummies with same name
  same_index_fruit = [colname for colname in fav_dummies.columns if fruit_name in colname]
  # Combining columns in course_dummies with same name
  fav_fruit[fruit_name] = pd.concat([fav_dummies[same_index_fruit]]).sum(axis=1)

# Dropping more unnecessary columns (if any)

fav_fruit = fav_fruit.drop(columns= [8,10,12,13,14,15,17])

# Renaming the first three column with 'name', 'age', 'sex'

fav_fruit.rename(columns={0:'name'}, inplace=True)
fav_fruit.rename(columns={2:'age'}, inplace=True)
fav_fruit.rename(columns={6:'sex'}, inplace=True)


# Printing the final table
print(fav_fruit)
