#################################################
# Python dictionary tutorial                    #
#################################################

# Initialize an empty dictionary
dictionary = {}

# Populate the dictionary using image names as keys and the
# car models as values
dictionary['0001.jpg'] = 'Ford Escape'
dictionary['0002.jpg'] = 'Subaru Outback'
dictionary['0003.jpg'] = 'Mazda Tribute'

# Will print the whole dictionary:
print(dictionary)

# Will only print the value of the dictionary with the key '0001.jpg'
print(dictionary['0001.jpg'])

# One way to loop through keys in a dictionary:
for imname in dictionary:
    print(imname, dictionary[imname])

# Another way to loop through a dictionary. Alternatively, you could set
# imagelist = dictionary.keys()

imagelist = ['0001.jpg', '0003.jpg']
for image in imagelist:
    print(image)
    label = dictionary[image]
    print(label)

# Example of looping through a list without using indices:
mylist = [1, 2, 3, 4, 5]
for item in mylist:
    print(item)
