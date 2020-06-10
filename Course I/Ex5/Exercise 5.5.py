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