# Exercise 5.3
import pandas as pd
pd.set_option('display.max_columns', 12)

# Reading the txt file (no header). This will give data with 1 column.
fav_fruit = pd.read_table('fav_fruits.txt')

# Splitting that column word by word. Use the pattern provided.
split_pattern = '[(\s+)(,\s+)]'

# Dropping unnecessary columns

# Replacing ['he','she'] with ['M','F']. Use pd.replace().


# Converting columns containing fruit names into dummy variable


# Reading txt file containing fruits list


# Combining columns consisting of dummy variable with same name


# Dropping more unnecessary columns (if any)


# Renaming the first three column with 'name', 'age', 'sex'


# Printing the final table
# print(fav_fruit)