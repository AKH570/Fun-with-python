class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year)+ ''+self.make + '' + self.model
		return long_name.title()

	def meter_reading(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
class ElectricCar(Car):
	def __init__(self,make,model,year):
		super(ElectricCar,self).__init__(make, model, year)
		
my_car = ElectricCar('Tesla','AX004',2018)
print(f'{my_car.get_descriptive_name()}')
my_car.meter_reading()