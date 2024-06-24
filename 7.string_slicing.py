# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]


car = "Supra MK4"

# first_name = car[0:5]
# shortHand
first_name = car[:5]

# last_name = car[-3:9] working
# last_name = car[-3:-1] not working
# shortHand
last_name = car[-3:]

funky_name = car[::3]

reversed_name = car[::-1]
 
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website1 = "http://google.com"
website2 = "http://youtube.com"
website3 = "http://facebook.com"

slicing = slice(7,-4)

print(website1[slicing],website2[slicing],website3[slicing])