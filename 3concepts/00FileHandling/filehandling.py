#file handling
#CRUD OPERATIONS

# Steps to follow when we want to read or write to files:
# 1. Open a file
# 2. Perform operations
# 3. close the file.


# Opening a file
# open() method returns a object (or) handler which we can use to handle the files.
f = open("message.txt")     # opening a file in current directory.
f = open("/home/yaswanth/Desktop/python_notes/3concepts/00FileHandling/message.txt")    #specifying full path.

# While opening, we have to specify operations we want to perform and mode(i.e., text or binary).
# By default, a file will be opened for reading in text mode.

"""
r	Opens a file for reading. (default)
w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	Opens a file for exclusive creation. If the file already exists, the operation fails.
a	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	Opens in text mode. (default)
b	Opens in binary mode.
+	Opens a file for updating (reading and writing)

"""

f = open("message.txt")     # equivalent to 'r' or 'rt' 
f = open("message.txt","w")     # write in text mode. 
f = open("message.txt","r+")     # read and write in text mode. 

# Binary mode is used to deal with non-text files like images (or) excutable files.

# The default encoding used is platform dependent. Its cp1252 for windows and utf-8 for linux.
#So, its a better idea to clearly specify encoding while opening files.
f = open("message.txt", mode='r',encoding='utf-8')     


# Closing a file.
# Once we are done with operations, we must close our files, So that the resources tied up with our files will be freed.
f.close()

#But Sometimes it may raise exceptions while closing files , if something goes wrong.
# So, a safer approach is using try....finally block.
try:
    f=open("message.txt",encoding='utf-8')
    #perform file operations
finally:
    f.close()

#But the best and recommended way to deal with opening and closing of files is to use with statement.
with open("message.txt", encoding='utf-8') as f:
    #perform file operations
    pass
# After complete execution of with block, file will be automatically closed.

# Writing to files in python.
with open("message.txt", 'w',encoding='utf-8') as f:   #it creates a tezt.txt file in current directory as it is not there.
    f.write("my first line\n")
    f.write("my second line\n")
    f.write("my last line\n")

with open("message.txt", 'r',encoding='utf-8') as f:
    #f.read(size)
    print(f.read(4))    #read the first 4 data.
    print(f.read(4))    #read the next 4 data.
    print(f.read())     #if size is not mentioned, it reads up to the end of the file.
    #At the end of the line, a new line character is also printed.
    print(f.read())     #once the end is reached, it returns empty string on further reading.

    print(f.tell())     #returns the current file cursor position in bytes.
    f.seek(0)            #brings file cursor to intial position.

    # We can read a file line-by-line using for loop.
    for line in f:
        print(line,end='')#the line in file, itself contains a new line character.So we use end='' to avoid two new lines while printing.
    
    f.readline()    #To read a line at a time.

