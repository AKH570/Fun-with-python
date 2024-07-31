 
num1 = input('Enter num1: ')
# if num1 == 'q':
num2 = input('Enter num2: ')
try:
	result = int(num1) + int(num2)
	print(f'result is : {result}')
except ValueError:
	print('Please enter numeric value')

