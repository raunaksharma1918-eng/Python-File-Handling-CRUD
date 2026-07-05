# CRUD = filehanding
# Create
# read
# update
# Delete

# from pathlib import 

# #Create
# filename = input('Enter your filename: ')
# with open(filename, 'w') as file:
#     content = input('Enter your content: ')
#     file.write(content)


"""
CRUD - File Handling
Create
Read
Update
Delete
Rename a file.
"""
import os
from pathlib import Path



#----CREATE-----
def create_file():
    filename = input('Enter your filename: ')#spiderman.txt
    path = Path(filename)#c:\users\tanishq\desktop\filehandling\superman.txt

    if path.exists():
        print('File already exists')
    else:
        with open(filename, 'w') as file:
            content = input('Enter your content: ')
            file.write(content)
            print('File Created...')

#---READ---
def read_file():
    filename = input('Enter your filename: ')#spiderman.txt
    path = Path(filename)#c:\users\tanishq\desktop\filehandling\superman.txt

    if path.exists():
        with open(filename, 'r') as file:
           print(file.read())
    else:
        print('File does not exists...')

#---DELETE---
def update_file():
    filename = input('Enter name of your file: ')
    path = Path(filename)
    if path.exists():
        with open(filename, 'a') as file:
            content = input('Enter your file cnotent: ')
            file.write(content)
            print('File updated sucessfully')
    else:
        print('File does not exists!!')

#---DELETE---
def delete_file():
    filename = input('Enter your file name: ')
    path = Path(filename)

    if path.exists():
        os.remove(path)
        print('File deleted sucessfully')
    
    else:
        print('File does not exists!!')

#----RENAME----
def rename_file():
    old_name = input('Enter your file name: ')
    path     = Path(old_name)

    if path.exists():
        new_name = input('Enter new name for your file: ')
        os.rename(old_name, new_name)
        print('File name changed..')

    else:
        print('File does not exists....')

#----FOLDER CREATE----
def create_folder():
    foldername = input('Enter name of folder: ')
    path = Path(foldername)

    if path.exists():
        print('Folder already exists')
    
    else:
        os.mkdir(foldername)
        print('Folder Created....')

#----DELETE FOLDER----
def delete_folder():
    foldername = input('Enter name of folder: ')
    path = Path(foldername)

    if path.exists():
        os.rmdir(foldername)
        print('Folder Created....')
    
    else:
        print('File does not exists!!')


while True:
    print("------Menu-----")
    print('Press 0 for exiting....')
    print("Press 1 for Creating a file")
    print("Press 2 for Reading a file")
    print("Press 3 for Updating a file")
    print("Press 4 for Deleting a file")
    print('Press 5 for Renaming a file')
    print('Press 6 for Creating a folder')
    print('Press 7 for Removing a folder')
    choice = int(input('Enter your choice: '))

    if choice == 0:
        print('Exiting...')
        break

    elif choice == 1:
        create_file()

    elif choice == 2:
        read_file()

    elif choice == 3:
        update_file()

    elif choice == 4:
        delete_file()

    elif choice == 5:
        rename_file()

    elif choice == 6:
        create_folder()

    elif choice == 7:
        delete_folder()