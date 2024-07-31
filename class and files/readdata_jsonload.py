import json

file1 = 'user_file.json' # json file name

with open(file1) as js:
	num = json.load(js)
print(num)

# Read from absolute path

path_link = 'E:/python_tricks/python_tricks-master/num.json'

with open(path_link,'r') as jr:
	num = json.load(jr)
print(f'Check the json data: {num}')