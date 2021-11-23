"""
Chapter 10

Files we might deal with as qa engineer
- yaml (similar to dictionaries)
- csv
- text
- xml
- json

Opening in Python:
open('C:/dev/basics/data/somefile'):
    # some code to do with file
    # read line by line
    alias_name.exit() or close the file

with open ('C:/dev/basics/data/somefile') as alis_name:
    #some
"""

# filepath = ".././../data/names.txt" #check folder way (./../../.)
# with open(filepath) as names:
#     #print(names.read())
#     print(names.readlines())  # creates the list from the rest of the lines
#     print(names.readline())  # first line
#     print(names.readline())  # second line
#     print(names.readline())  # third line
#     print(names.readline())  # fourth line
#     print(names.name)  # return the name of the file

myfile = ".././../data/names.txt"

def read_file_lines(filepath):
    try:
        with open(filepath) as data:
            for line in data.readlines():
                print('line value', end="")
    except FileNotFoundError as err:
        print(f"Please check your file path.\n{err}")


read_file_lines(myfile)
print("#### Completed!")