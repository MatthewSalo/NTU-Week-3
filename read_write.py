# Testing out a reading function
def read():
  try:
    my_file = open ("datafile.txt", "r")
    for line in my_file.readlines():
      print(line)
  finally:
    my_file.close()

# Testing out a write function
def write():
  try:
    my_file = open("data.txt", "w") # Creates file if it doesn't exist
    for i in range(10):
      my_file.write("This is line {} \n".format(i)) # Print 10 lines
  finally:
    my_file.close()

# Check if file or directory exists
def check_file():
  import os
  filename = input("What file do you want to check? ")
  path = os.path.dirname(os.path.abspath(filename))
  print(os.path.isfile(filename)) # True if the file exists, otherwise False
  print(os.path.isdir(path)) # True if the directory exists
  print(path)

check_file()