#def show_magicians(names):
   # """print a simple greeting to each magician in the list."""
   # for name in names:
       # msg= "Hello, " + name + "!"
        #print(msg)

#magicians= ['law', 'vegapunk', 'mog']
#show_magicians(magicians)

#magicians=['law', 'vegapunk', 'mog']
#greetings=[]
#while magicians:
    #greeting= magicians.pop()
    #print("The great: " + greeting)
    #greetings.append(greeting)

#print("\nThe following magicians are great:")
#for greeting in greetings:
    #print(greetings)

#def make_great(magicians, greetings):
    #"""Simulate greeting to each magician"""
    #"""Move each greeting after printing"""
    #while magicians:
       # greeting = magicians
        #print("Great Magician: " + greeting)
       # greetings(greeting)

#def show_magicians(greeting):
   # """Greet all magicians as great"""
    #print("\nThe following magicians are great: ")
    #for greeting in greeting:
        #print(greeting)

#magicians= ['law', 'vegapunk', 'mog']
#greetings=[]

#print(magicians, greetings)
#show_magicians(greetings)
#print(magicians[:], greeting)

#def make_sandwich(*items):
    #"""Summarize the sandwich we are about to make."""
    #print("\nMaking a sandwich with the following items: ")
    #for item in items:
       # print(item)

#make_sandwich('vegan eggs')
#make_sandwich('vegan cheese')
#make_sandwich('tofu')

#def build_profile(first,last, **user_info):
   # """Build a dictionary containing everything we know about a user."""
   # profile={}
   # profile['first_name'] = first
   # profile['last_name'] = last
   # for k,v in user_info.items():
       # profile[k]=v
   # return profile
    
#user_profile = build_profile('Monkey', 'Muffy', 
                            #location= 'Metaverse', 
                           # career = 'Softaware Engineer')

#print(user_profile)

def car_desciption(manufactuer, model, **car_ifo):
    """Build a dictionary containing everything we know about a car."""
    car={}
    car['manufactuer'] = manufactuer
    car['model'] = model
    for k,v in car_ifo.items():
        car[k]=v
    return car

car_d= car_desciption('subaru', 'outback', color='blue', tow_package=True)
print(car_d)
car_de= car_desciption('corvette', 'chevorlet', color= 'silver', strips= True)
print(car_de)


