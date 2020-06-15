# Assignment V
# Do not alter the dataset or arrange the file manually.

# Exercise 5.5
import numpy as np
import pandas as pd
import re 

from pathlib import Path
from datetime import datetime, timedelta 

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

#movie_df

movie_df=pd.DataFrame()

movie_path1 = Path('.') / 'movies' / 'movie_set1'
file_movie_paths1 = list(movie_path1.iterdir())

for i in list(file_movie_paths1):
  movie_read = pd.read_csv(i, sep= ',', index_col=False)
  movie_df = movie_df.append(movie_read, ignore_index = True)

movie_path2 = Path('.') / 'movies' / 'movie_set2'
file_movie_paths2 = list(movie_path2.iterdir())

for i in list(file_movie_paths2):
  movie_read = pd.read_csv(i, sep= ',', index_col=False)
  movie_df = movie_df.append(movie_read, ignore_index = True)

movie_path3 = Path('.') / 'movies' / 'movie_set3'
file_movie_paths3 = list(movie_path3.iterdir())

for i in list(file_movie_paths3):
  movie_read = pd.read_csv(i, sep= ',', index_col=False)
  movie_df = movie_df.append(movie_read, ignore_index = True)

movie_path4 = Path('.') / 'movies' / 'movie_set4'
file_movie_paths4 = list(movie_path4.iterdir())

for i in list(file_movie_paths4):
  movie_read = pd.read_csv(i, sep= ',', index_col=False)
  movie_df = movie_df.append(movie_read, ignore_index = True)

movie_path5 = Path('.') / 'movies' / 'movie_set5'
file_movie_paths5 = list(movie_path5.iterdir())

for i in list(file_movie_paths5):
  movie_read = pd.read_csv(i, sep= ',', index_col=False)
  movie_df = movie_df.append(movie_read, ignore_index = True)


#rating_df

rating_df = pd.DataFrame()

rating_path = Path('.') / 'ratings' 
file_rating_paths = list(rating_path.iterdir())

for i in list(file_rating_paths):
  rating_read = pd.read_csv(i, sep= ',')
  rating_df = rating_df.append(rating_read, ignore_index = False)


# No. 1

avg_rating_df = rating_df.groupby(['movieId']).mean()
avg_rating_df = avg_rating_df.drop(columns=['userId','timestamp'])

avg = movie_df.set_index('movieId').join(avg_rating_df)

avg = avg.drop(columns=['genres','year'])
avg = avg.rename(columns={'rating': 'average rating'})

#print(avg)

#print("AVERAGE_RATING")
#print(avg.columns)


# No. 2

rating_count_df = rating_df.groupby(['movieId']).count()
rating_count = movie_df.set_index('movieId').join(rating_count_df)
rating_count = rating_count.drop(columns=['genres','year','userId','timestamp'])
rating_count = rating_count.rename(columns={'rating': 'the number of ratings'})

#print("RATING_COUNT")
#print(rating_count)


# No. 3

letter=[]

for a_string in rating_count['title'].values:
  letter_fix = re.sub("[\(\[].*?[\)\]]", "", a_string)
  number_of_letters = len(letter_fix) - a_string.count('"')
  
  letter.append(number_of_letters)

letter_df = pd.DataFrame(letter) 

letter_count = movie_df.join(letter_df)
letter_count = letter_count.drop(columns=['genres','year',])
letter_count = letter_count.rename(columns={0: 'length of title'})

#print(letter_count)


# No. 4

user_rating_df = rating_df.groupby(['userId']).count()
user_rating_df = user_rating_df.drop(columns=['movieId','timestamp'])
user_rating_df = user_rating_df.rename(columns={'rating': 'the number of ratings'})

#print(user_rating_df)


# No. 5

user_genres_rating_df = rating_df.set_index('movieId').join(movie_df)
user_genres_rating_df = user_genres_rating_df.drop(columns=['year','title','timestamp','movieId'])

user_genres_rating_df = user_genres_rating_df.sort_values(by=['userId'])

user_genres_rating_df = user_genres_rating_df.groupby(['userId', 'genres']).count() 

user_genres_rating_df = user_genres_rating_df.rename(columns={'rating': 'number of ratings by genres'})

#print(user_genres_rating_df)


# No. 6

user_avg_rating_df = rating_df.groupby(['userId']).mean()
user_avg_rating_df = user_avg_rating_df.drop(columns=['movieId','timestamp'])
user_avg_rating_df = user_avg_rating_df.rename(columns={'rating': 'average ratings'})


#print(user_avg_rating_df)


# No. 7

user_period_list = []

user_period_max = rating_df.groupby(['userId']).max()
user_period_min = rating_df.groupby(['userId']).min()

user_period_max_df = user_period_max['timestamp'].values
user_period_min_df = user_period_min['timestamp'].values

for i in range (len(user_period_max_df)):
  user_period_list.append((datetime.fromtimestamp(user_period_max_df[i]) - datetime.fromtimestamp(user_period_min_df[i])).days)

user_period = pd.DataFrame(user_period_list)
user_period_df = user_avg_rating_df.reset_index()
user_period_df = pd.concat([user_period_df, user_period], axis=1)
user_period_df = user_period_df.drop(columns=['average ratings'])
user_period_df = user_period_df.rename(columns={0: 'longest period (days)'})

#print(user_period_df)


# No. 8

year_df = movie_df.groupby(['year']).count()
year_df = year_df.drop(columns=['movieId','title'])
year_df = year_df.rename(columns={'genres': 'number of movies'})

#print(year_df)

# No. 9

year_high = rating_df.groupby(['movieId']).mean()
year_high_df = movie_df.set_index('movieId').join(year_high)
year_high_df = year_high_df.drop(columns=['genres','userId','timestamp'])

year_high_df = year_high_df.groupby('year').apply(lambda x: x.loc[x.rating == x.rating.max(),['rating','title']])

year_high_df = year_high_df.rename(columns={'rating': 'average rating'})


#print(year_high_df)


# No. 10

genres_dummy = pd.get_dummies(movie_df['genres']).corr()

genres_dummy = np.round(genres_dummy,3)

#print(genres_dummy)



# Writing to csv


avg.to_csv('top10/01. Movies with average ratings.csv')

rating_count.to_csv('top10/02. Movies with the number of ratings each gets.csv')

letter_count.to_csv('top10/03. Movies with the length of their title.csv')

user_rating_df.to_csv('top10/04. User Ids with the number of ratings.csv')

user_genres_rating_df.to_csv('top10/05. User Ids with the number of ratings each genres categories.csv')

user_avg_rating_df.to_csv('top10/06. User Ids with the average ratings they give.csv')

user_period_df.to_csv('top10/07. User Ids with the longest period of giving ratings.csv')

year_df.to_csv('top10/08. Years with number of movies in that year.csv')

year_high_df.to_csv('top10/09. Years with movies of the highest (average) ratings in that year.csv')

genres_dummy.to_csv('top10/10. All pairs of movies genre with their correlation.csv')




# Writing Top 10 of each

print("Top 10 of Movies from the highest average ratings\n")
print(avg.nlargest(10, 'average rating'))

print("\n\nTop 10 of Movies from the most number of ratings\n")
print(rating_count.nlargest(10, 'the number of ratings'))

print("\n\nTop 10 of Movies from the longest length of title\n")
print(letter_count.nlargest(10, 'length of title'))

print("\n\nTop 10 of User Ids with the most number of ratings\n")
print(user_rating_df.nlargest(10, 'the number of ratings'))

print("\n\nTop 10 of User Ids with the most number of ratings given in each genres categories\n")
print(user_genres_rating_df.nlargest(12, 'number of ratings by genres'))

print("\n\nTop 10 of User Ids with the highest average ratings they give\n")
print(user_avg_rating_df.nlargest(10, 'average ratings'))

print("\n\nTop 10 of User Ids with the longest period of giving ratings\n")
print(user_period_df.nlargest(10, 'longest period (days)'))

print("\n\nTop 10 of Years with the most number of movies in that year.\n")
print(year_df.nlargest(10, 'number of movies'))

print("\n\nTop 10 of Years with movies of the highest (average) ratings in that year.\n")
print(year_high_df.nlargest(65, 'average rating'))

print("\n\nTop 10 of pairs of movie genre with highest correlation.\n")

genres_df = genres_dummy.unstack()
genres_top = genres_df.sort_values(kind="quicksort")
genres_20 = genres_top.head(20)
genres_10 = genres_20[::2]
print(genres_10)



