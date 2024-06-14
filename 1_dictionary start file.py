import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

'''

print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))

print(len(phonebook)) #tells u amount of pairs in dictionary
mydict=dict(m=8,n=9) #dict function allows us to give key value pairing in that format

print(mydict)

print(phonebook['Chris']) #we would get phone number from this because we are giving it the KEY
phoneno=phonebook['Chris'] #phoneno is a STRING object and it will give back chris's phone number

print(phoneno) 

print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()


name='chris'

if name in phonebook:#the default search option for dictionary is the KEYS
    print(phonebook)
else:
    print(f'{name} not found in phonebook')




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

#a dictionary is a MUTABLE object: it can be changed, BUT u CANNOT edit an existing key

print(phonebook) 
phonebook['Chris']='555-4444'
phonebook['Joe']='555-0123'

print(phonebook) #chris's number was updated and we have new entry for Joe
#if a key exists, it'll update the value with what u give it, but if it doesnt exist, then itll append it to the dictionary






print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook['Chris'] #this is how u delete a dictionary pair
print(phonebook)




print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()
#we can loop through keys and values
#dictionary is an iterable object , and u can loop to iterate through each pair in a dictionary

for key in phonebook:
    print(f' the key is: {key} and the value is {phonebook[key]}') # itll return the corresponding value to each key
    
for value in phonebook.values(): #how we cycle thru all the values using the values 
    #(the .values is a method that belongs to dictionary object, and allows us to print out and access the values of keys

    print(value)
for k,v in phonebook.items():
    print(k,v) #the .items method returns a tuple with multiple values, and it splits it up
#assigns to corresponding variable

for item in phonebook.items():
    print(item) #each tuple has two elements in it, so giving it one element will get back one object




print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

#it gives default value if key is not found
phone=phonebook.get('Chris','key not found') #itll say key not found if the key u look for doesnt exist
print(phone)

phonebook.clear() #it clears out the contents so that ur dictionary is empty
print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


#it pops out key value pair from dictionary so that when ur done w it it doesnt remain in the dictionary

print(phonebook)
remove=phonebook.pop('Chris','not found') #default method if doesnt exist
print(remove) #its NOT deleted, it pops out the pair and it allows us to do what we want w the variable
print(phonebook)


print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#it randomly selects a key value pair from ur dictionary, and pop it out
#the random part of this method doesn't work
#

a=phonebook.popitem()
print(a)
print(phonebook) 
#its just popping out the last item in ur dictionary, it doesn't randomly select it




print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()



list_of_keys=list(phonebook) #this creates a list of the keys
print(list_of_keys)
#random_key=random.choice(list_of_keys) #allows u to pick random index in list
#print(random_key)

print(phonebook[random.choice(list(phonebook))])








print()
print('*****  end section 9 ********')
print()








