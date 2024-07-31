# Writing to an Empty File: To write text to a file, you need to call open() with a second argument telling 
# Python that you want to write to the file.
# The call to open() in this example has two arguments.
# The second argument, 'w', tells Python that we want to open the file in write mode.
# we use the write() method on the file object to write a string to 
#the file. 
#This program has no terminal output.
'''
file_path = 'E:/python_tricks/python_tricks-master/write_file_for_py.txt'
with open(file_path,'w') as wf:
	wf.write('Welcome to this file! Here it is write messages.')
'''
# Writing Multiple Lines:
file_path= 'E:/python_tricks/python_tricks-master/write_multiline.txt'
with open(file_path,'w') as wf:
	wf.write('Welcome to this file!\n')
	wf.write(' Here it is new line messages.\n')

# Appending to a File: 
# use the 'a' argument to open the file for appending rather 
# than writing over the existing file
file_path= 'E:/python_tricks/python_tricks-master/write_multiline.txt'
with open(file_path,'a') as wf: 
	wf.write('Name is Md. Abir Hossain Khandokar.\n')
	wf.write('come from Naogaon.\n')