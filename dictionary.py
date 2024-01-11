#person= {
    #'first_name': 'Trafalgar D.',
    #'last_name': 'Water Law',
    #'age': '26',
    #'city': 'Flevance',
#}

#print(person ['first_name'].title())
#print(person ['last_name'].title())
#print(person ['age'].title())
#print(person ['city'].title())

#numbers= {
    #'muffy': '17',
    #'mk': '222',
    #'jm': '333',
    #'moon': '444',
    #'aang': '555',
#}

#print( "muffy's favorite number is" , numbers['muffy'].title()+ ".")
#print("mk's favorite number is" , numbers['mk'].title()+ ".")
#print("jm's favorite number is" , numbers['jm'].title()+ ".")
#print("moon favorite number is" , numbers['moon'].title()+ ".")
#print("aang favorite number is" , numbers['aang'].title()+ ".")

#glossary= {
    #'list': 'allow you to move every element at once or same amount of an element',
    #'concatenation': 'to replicate',
   # 'loop': 'sets of info in one place',
    #'dictionary': 'limitless amount of info in a location',
    #'tuple': 'lists that cant be change',
    #'set': 'each item that you are moving must be unique.',
    #'!=' : 'determines whether two values are equal or not.',
    #'conditional tests' : 'true or false statements',
    #'float' : 'any number with a decimal.',
    #'append' : 'add a item to a list.',
#}


#print("Concatenation means", glossary['concatenation'].title()+ "." '\n')
#print("The defintion of lists means to" , glossary['list'].title()+ "." '\n')
#print("Tuples are" , glossary['tuple'].title()+ "." '\n')
#print("Loops are" , glossary['loop'].title()+ "." '\n')
#print("Right now we are learning about dictionaries, dictionaries are" , glossary['dictionary'].title()+ "." '\n')

#for defintion in set (glossary):
    #print(glossary)

#rivers= {
    #'nile': 'egypt',
    #'amazon': 'brazil',
    #'yangtze': 'china',
#}

#for river in set(rivers):
    #print("The Nile runs through" , rivers['nile'] + ".")
    #print("The Yangtze River runs through", rivers['yangtze']+ ".")
    #print("The Amazon River runs through" , rivers['amazon']+ "." '\t\n')

#for river in rivers.keys():
    #print(river.title())
#print('\t\n')

#for country in rivers.values():
    #print(country.title())

#favorite_languages= {
    #'muffy': 'css',
    #'jen': 'python',
    #'law': 'html',
    #'edward': 'ruby',
    #'sarah': 'c',
    #'phil': 'js',
#}

#for name in sorted(favorite_languages.keys()):
    #print(name.title()+ ", thank you for taking the poll.")

#if 'zoro' not in favorite_languages.keys():
    #print("Zoro, you should take our poll!")

people= {
    'Muffy': {
        'first': 'Monkey',
        'last': 'Muffy',
        'age': '19',
        'city': 'Foosha',
    },
    "TC": {
        'first' : 'Tony Tony',
        'last' : 'Chopper',
        'age': '17',
        'city': 'Drum',
    },
}  
for name, people_info in people.items():
    print("\nName: " + name)
    full_name = people_info['first'] + " " + people_info['last']
    age = people_info['age']
    location = people_info['city']

print("\tFull name: " + full_name.title())
print("\tAge: " + age.title())
print("\tLocation: " + location.title())


