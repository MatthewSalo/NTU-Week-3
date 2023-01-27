def openbook():
    import os # import os

    filename = "pg1342.txt" # file name of text document
    path = os.path.abspath(filename) # path of text document using os.path
    print("The file name is ",filename,"\nThe path of the file is ",path,"\n")
    try:
        my_file = open(filename,"r",1,'UTF-8') # open filename as read and using 1 as buffering and UTF-8 as encoding arguments
        for line in my_file.readlines():
            if 'Chapter' in line:
                print(line)

    finally:
        my_file.close()

# Calls function openbook
openbook()