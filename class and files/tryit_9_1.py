# Make a class Restaurant
class Restaurant():
	''' model of Restaurant'''
	def __init__(self,restaurant_name,cuisine_type):
		'''initialize restaurant_name and cuisine_type attributes'''
		self.restaurant_name=restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print(f'\nThe {self.restaurant_name} restaurant serve quality food.')
		print(f'You will get always new test from {self.restaurant_name}.')
	
	def open_restaurant(self):
		print(f'The {self.restaurant_name.title()} is open at 7.30am daily.')

restaurant = Restaurant('STAR','Chinees')

print(f'Welcome to {restaurant.restaurant_name}!')
print(f'All {restaurant.cuisine_type} foods are available here.')

restaurant.describe_restaurant()
restaurant.open_restaurant()

