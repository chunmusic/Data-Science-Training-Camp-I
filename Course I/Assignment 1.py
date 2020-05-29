# Students No. : C0IM4022

# Assignment I

# 1 
import pandas as pd
import numpy as np
pd.set_option('mode.chained_assignment', None)


print("Test 1")
movie = pd.read_csv("movie.csv")

# 2
print("Test 2")
budget = movie[["budget"]]
budget_avg = budget.mean()
print("The average budget of all the movies is " + str(budget_avg) + "USD.")

# 3
print("Test 3")
diff_director = movie[["director_name"]].drop_duplicates()
print("The number of different directors in the dataset is " + str(len(diff_director)) + ".")

# 4
aspect_ratio = movie[["aspect_ratio"]]
aspect_ratio = aspect_ratio.fillna(2.35)
movie[["aspect_ratio"]] = aspect_ratio

# 5
movie = movie.dropna(subset=['budget', 'imdb_score','title_year'])


# 6
movie = movie.drop(movie[movie.title_year < 1990].index)

# 7
director_budget = movie[['director_name','movie_title','budget','imdb_score','title_year']]


# 8
print("Test 8")
sum = director_budget.groupby("director_name").sum()

director_budget["director_expense"] = ""


for j in (director_budget.index):
  
  for i in range (len(sum.index)):

    if director_budget.director_name[j] == sum.index[i]:
      director_budget.at[j, 'director_expense'] = sum.budget[i]

print(director_budget)

# 9
print("Test9")
director_budget = director_budget.groupby("director_name").describe()
print(director_budget)


# 10

director_budget.to_csv('dir_budget.csv', index = False, header=True)



