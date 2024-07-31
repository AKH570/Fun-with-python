def Greet_msg():
	print('hello Abir')
Greet_msg()

# passing information to function

def Greet_msg(name): # ----> Parameter "name"
	print(f'Hello {name}! How are you?')
Greet_msg('Abir') # -----> Arguments "Abir"
Greet_msg('Jack')

# Three type of function: positional arguments and keyword arguments
# Positional Arguments: Which need to be in the same order the parameter were written

def persone_details(name,education):
	print(f'I am {name} and my education is {education}')
	# print(f'my education is {education}')
persone_details('Abir','Honors')

# Keyword Arguments: A keyword argument is a name-value pair that you pass to a function. You 
# directly associate the name and the value within the argument
# When you use keyword arguments, be sure to use the exact names of the parameters in 
# the function’s definition.

def persone_details(name,education):
	print(f'Hi I am {name}, and my edu is {education}')
persone_details(education='Bsc',name='Abir')

# default value : When writing a function, we can define a default value for each parameter.
# you define a default value for a parameter, you can exclude the corresponding argument you’d usually write in the function call

def persone_details(name,education='BSC'): # --> default value of education
	print(f'Hi I am {name}, and my edu is {education}')
persone_details(name='Abir')

def persone_details(name,education='BSC'): # --> default value of education
	print(f'Hi I am {name}, and my edu is {education}')
persone_details('Ratan') # ---> as a positional arguments

# Return Value: The return statement takes a value 
# from inside a function and sends it back to the line that called the function.abs
# When you call a function that returns a value, you need to provide a 
# variable where the return value can be stored.

def return_value(first_name,last_name):
	full_name = first_name + ' ' + last_name
	return full_name
name = return_value('Abir','Khandokar')
print(name)

# Making an Argument Optional : 
def return_value(first_name,last_name,mid_name=''): #--->mid_name is optional here
	full_name = first_name + ' ' + last_name + ' ' + mid_name
	return full_name
name_as = return_value('Abir','khandokar','Hossain')
print(f'mid_name is optional: {name_as}')

# using if condition
def return_value(first_name,last_name,mid_name=''): #--->mid_name is optional here
	if mid_name:
		full_name = first_name + ' ' + last_name + ' ' + mid_name
	else:
		full_name = first_name + ' '+ last_name
	return full_name
name_as = return_value('Abir','khandokar')
print(f'mid_name is optional: {name_as}')

# Returning a Dictionary: function takes in parts of a name and returns a dictionary.

def return_dict(first_name,last_name):
	full_name = {'firstName':first_name,
				'lastName':last_name}
	return full_name
name_as_dict = return_dict('Abir','khandokar')
print(f'name_as_dict:{name_as_dict}')

# using uptional argument

def return_dict(first_name,last_name,mid_name=''):
	full_name = {'firstName':first_name,
				'lastName':last_name,
				'midName':mid_name}
	if mid_name:
		full_name['midName']=mid_name
	return full_name
name_as_dict = return_dict('Abir','khandokar','Hossain')
print(f'adding_lastName_as_dict:{name_as_dict}')

# Passing a List: as arguments
def passing_list (names):
	for n in names:
		print(f'my first name is:{n}')

nameas = ['Abir','hossain','40']
passing_list(nameas)

# Passing an Arbitrary Number of Arguments : Python allows a function to collect an arbitrary number of arguments from the calling statement.
#The asterisk in the parameter name *names tells Python to make an 
#empty tuple called names and pack whatever values it receives into this 
#tuple.
def arbtr_func(*names):
	print(f'This is arbitrary function exp: {names}')
arbtr_func('Abir','hossain',80)

# print using for loop

def arbtr_func(*foods):
	for food in foods:
		print(f'food name:- {food}')
arbtr_func('rice')
arbtr_func('chicken','salad','motton','vegi')

# Mixing Positional and Arbitrary Arguments: If a function to accept several different kinds of arguments,
# the parameter that accepts an arbitrary number of arguments must be placed 
# last in the function definition.

def mixArbtr_posi(qnty,*foods):
	print(f'Food quantity:{qnty} and foods are {foods}')
mixArbtr_posi('rice',3)
mixArbtr_posi(5,'chicken','salad','motton','vegi')

#  Arbitrary Keyword Arguments: Sometimes you’ll want to accept an arbitrary number of arguments, but you 
# won’t know ahead of time what kind of information will be passed to the 
# function.
# The double asterisks before the parameter **info cause Python to create 
# an empty dictionary called 'info' and pack whatever name-value pairs it 
# receives into this dictionary. 
def arbtr_keyword_argu(first_name,last_name,**info):
	profile_info = {}
	profile_info['name1']=first_name
	profile_info['name2'] = last_name

	for key, value in info.items():
		profile_info[key]=value
	return profile_info
profile = arbtr_keyword_argu('Abir','Hossain',edu='MSc',year='2008')
print(f'arbitrary keyword: {profile}')
