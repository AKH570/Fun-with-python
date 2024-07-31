# Reading an Entire File: 
# To do any work with a file, even just printing its contents, you first need to open the file to access it.The open() function needs 
# one argument: the name of the file you want to open.
# The keyword 'with' closes the file once access to it is no longer needed.
with open('pi.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

	# File Paths:
# When you pass a simple filename like pi_digits.txt to the open() function, 
# Python looks in the directory where the file that’s currently being executed 
# (that is, your .py program file) is stored
		# relative path
with open('file_reader\pi_file.txt') as pi:
	storefile = pi.read()
	print(f'contents of file: {storefile}')
		# absolute file path
# Absolute paths is being stored in a variable and then pass that variable to open().
# Using absolute paths, you can read files from any location on your system.
# In this case you should use forward slash for this path.
# Windows OS they look like this:
path_link = 'E:/python_tricks/iconmoon_add.txt'
with open(path_link) as ap:
	contents = ap.read()
	print(f'contents of file from absolute path: {contents}')

# Reading Line by Line:
# You might be looking for certain information in the file, or you might want to 
# modify the text in the file in some way.
# use a for loop on the file object to examine each line from a 
# file one at a time.

file_path = 'E:/python_tricks/python_tricks-master/read_file_for_py.txt'
with open(file_path) as fl:
	for i in fl:
		print(f'line of content: {i.strip()}')

# Making a List of Lines from a File:
# the readlines() method takes each line from the file and stores it 
# in a list
file_path = 'E:/python_tricks/python_tricks-master/read_file_for_py.txt'
with open(file_path) as ml:
	# readlines() store the data in list[]
	lines = ml.readlines() 
	print(f'readlines:{lines[4:5]}') 

for line in lines: # to print each line use for loop
	print(f'line only: {line}') 

# Working with a File’s Contents:
# After you’ve read a file into memory, you can do whatever you want with 
# that data,
# we’ll attempt to build a single string..abs

file_path = file_path = 'E:/python_tricks/python_tricks-master/read_file_for_py.txt'
with open(file_path) as pa:
	lines = pa.readlines()
# we will make a single string of the file content
line_string = ''
name = ''
for line in lines[0:1]:
	line_string +=line.rstrip() # rstrip() removes the newline character from each line
	print(f'one line print:{line_string}')
	name=line_string.replace('Abir', 'Ayan')
print(f'line string are: {name}')
print(f'length of single string:{len(line_string)}')