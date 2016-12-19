# 1. Importing a multiple Classes from a Module
from car import Car, ElectricCar

# 2. Importing an entire Module
import car

# 1.
my_bettle = Car('volkswagen', 'beetle', 2016)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

print("\n")
# 2.
my_bettle = car.Car('volkwagen', 'beetle', 2016)
print(my_bettle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
