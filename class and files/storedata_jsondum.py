import json
# to write data in memory using json.dum()
user_file = [1,2,3,4,5,6,7,22,90,34,54,54,35]

file1 = 'user_file.json' # give the file name with json that to be stored in file1

with open(file1,'w') as js: # 1st argument is file name
	# json.dump() function takes two arguments:
	# a piece of data to store and a file object it can use to store the data.
	json.dump(user_file,js)

# Absolute path
num = 1,2,3,4,5,6,7,7,8,9,11,12,32,43,54,64
path_link ='E:/python_tricks/python_tricks-master/num.json'
with open(path_link,'w') as jw:
	json.dump(num,jw)