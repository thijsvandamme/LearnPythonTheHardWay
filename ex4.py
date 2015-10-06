# assign 100 to the name cars
cars = 100
#assign a floating point to then name space_in_a_car
space_in_a_car = 4.0
#make variable drivers
drivers = 30
#make variable passengers
passengers = 90
#make a variable and fill it with a substraction of 2 other variables and their contents
cars_not_driven = cars - drivers
#give a variable the value of another variable
cars_driven = drivers
#make variable and assign it with a multiplication of 2 other variables
carpool_capacity = cars_driven * space_in_a_car
#make variable and assign it with a division of 2 other variables
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have,", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

