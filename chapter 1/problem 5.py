import os  # Import the os module to interact with the operating system

 #Specify the directory path you want to list. '.' represents the current directory
directory_path = '.'

 #Use os.listdir() to get a list of all files and directories in the specified path
contents = os.listdir(directory_path)

#Print a header for clarity
print("Contents of the directory:")

#Iterate over each item in the contents list and print it
for item in contents:
    print(item)
