#sandwich_order = ['grilled cheese', 'egg sandwich', 'chicken sandwich', 'ice cream sandwich', 'tuna sandwich']
#finish_sandwiches=[]
#while sandwich_order:
    #finish_s = sandwich_order.pop()
    
    #print("Finish Sandwiches: " + finish_s.title())
    #finish_sandwiches.append(finish_s)
    #print("\nThe folowing sandwiches have been made:")
#for finish_sandwiches in finish_sandwiches:
    #print("\nI made your , " + finish_sandwiches + " sandwich")

#sandwich_order = ['grilled cheese', 'pastrami','egg sandwich', 'chicken sandwich', 'pastrami', 'ice cream sandwich', 'tuna sandwich', 'pastrami']
#print("We are out of pastrami, sorry for the incovenience.")
#while 'pastrami' in sandwich_order:
    #sandwich_order.remove('pastrami')
#print(sandwich_order)

from http.client import responses


dream= {}
polling_active= True

while polling_active:
    name = input("\nWhat is your name? ")
    respose = input("If you could visit one place in the world, where would you go? ")
    responses[name] = respose
    repeat= input( "Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active= False
        print("\n---Results---")
for name, respose in responses.items():
    print(name , " would like to travel to " + respose + ".")

    #no idea why the final statement kept messing up.