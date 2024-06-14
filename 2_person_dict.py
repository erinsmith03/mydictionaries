person = {}
person["fname"] = "Joe" #this key value pair is now added to dictionary
print(person) # at this point, the first one was the only pair added
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #the value of a key could be any object! this is a list
person["pets"] = {"dog": "Fido", "cat": "Sox"} #the value is a dictionary... so we have a dictionary within a dictionary

print(person)
#if ur dealing with a list, give it index value, if ur dealing with dictionary, give it key
#print(person)

# print out the name of the second child
print(person['children'][1])


# print out the name of the cat

print(person['pets']['cat']) #give it the key of the dicionary


# use a loop to print out the names of each child

for name in person['children']:
    print(name)


# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

mydict=person['pets']
print(mydict)
for pet,name in mydict.items():
    print(f'The type of pet is: {pet} and the name of the pet is {name}')

