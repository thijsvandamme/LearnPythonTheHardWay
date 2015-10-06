name = 'Thijs Van Damme'
age = 35 
height = 74 # inches
weight = 180 #lbs
eyes = 'Green & Brown'
teeth = 'White'
hair = 'Blond'

weight_in_kg = weight * 0.453592
height_in_cm = height * 2.54



print "Lets talk about %s." % name
print "He's %d inches / %d cm tall." % (height, height_in_cm)
print "He's %d pounds / %d kg heavy" % (weight, weight_in_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d and %d I get %d." % (age,height,weight,age + height + weight)
