from pathlib import Path
import os

def create_folder():
    try:
        name = input("Enter the folder name: ")
        p = Path(name)
        p.mkdir()
        print(f"folder created as {p}")
    except Exception as err:
        print(f"Sorry an error occured as {err}")

def read_file_folder():
    p = Path("")
    items = list(p.rglob('*'))
    for i, v in enumerate(items):
        print(f"{i + 1} : {v}")
    

print("Options:- ")

print("1. Create a folder")
print("2. Read files and folders")
print("3. Update the folder")
print("4. Delete the folder")

choice = int(input("Please chosse your option: "))


if choice == 1:
    create_folder()