class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'\nThe {self.restaurant_name} restaurant serve quality food.')
		print(f'You will get always new test from {self.restaurant_name}.')

restaurant1 = Restaurant('STAR','Chinees')
restaurant2 = Restaurant('SULTAN','Kacci')
restaurant3 = Restaurant('PIZZHAT','Pizza')

print(f'Welcome to {restaurant1.restaurant_name}. Please order your {restaurant1.cuisine_type} food')
print(f'Welcome to {restaurant2.restaurant_name}. Please order your {restaurant2.cuisine_type} food')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()