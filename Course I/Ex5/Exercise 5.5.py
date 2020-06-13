# You might need to refresh this page when making a new folder
from pathlib import Path

print("Checking if there's a file called 'text2.txt' in 'folder1'")
file_path = Path('.') / 'folder1' / 'text2.txt'
print(file_path.exists())

print("\nChecking if there's a directory called 'folder3'")
file_path = Path('.') / 'folder3'
print(file_path.exists())

print("\nGetting all files with .csv extension.")
dir_path = Path('.') / 'folder1'
file_paths = dir_path.glob("*.csv")
print(list(file_paths))

print("\nGetting all .txt files starts with 'other' in all directories.")
dir_path = Path('.')
file_paths = dir_path.rglob("other?.txt")
print(list(file_paths))

print("\nMaking a folder called 'folder_new_1' inside 'folder_new")
dir_path = Path('.') / 'folder_new' / 'folder_new_1'
dir_path.mkdir(parents=True)

print("\nRenaming 'folder_new_1' with 'folder_n1'")
dir_path = Path('.') / 'folder_new' / 'folder_new_1'
dir_path.rename(dir_path.parent / 'folder_n1')

print("\nReplacing 'folder_n1' with 'folder_1'")
dir_path = Path('.') / 'folder_new' / 'folder_n1'
dir_path2 = Path('.') / 'folder1'  
dir_path.replace(dir_path.parent / dir_path2)


# Exercise 5.5
import numpy as np
import pandas as pd

from pathlib import Path

df_append=pd.DataFrame()

file_path = Path('.') / 'folder_new' 
file_path.mkdir()

df1 = pd.read_csv('folder1/data1.csv', sep=',')
df2 = pd.read_csv('folder1/data2.csv', sep=',')

df = df1.append(df2, ignore_index = True) 

df.to_csv('folder_new/data.csv')


dir_path1 = Path('.') / 'folder1'
file_paths1 = dir_path1.rglob("text?.txt")

for i in list(file_paths1):
  print(i)
  df_txt = pd.read_csv(i, sep= ',')
  df_append = df_append.append(df_txt, ignore_index = True)


dir_path2 = Path('.') / 'folder2'
file_paths2 = dir_path2.rglob("text?_2.txt")

for j in list(file_paths2):
  df_txt = pd.read_csv(j, sep= ',')
  df_append = df_append.append(df_txt, ignore_index = True)

print(df_append)

df_append.to_csv('folder_new/text_combined.csv')

