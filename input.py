#rental_car= input("What kind of rental car would you like? ")
#print("Let me see if i can find, " + rental_car + "!")

#seating= input("How many people are in their dinner group? ")
#seating= int(seating)

#if seating >= 8:
    #print("\nYou have to wait for a table.")
#else:
    #print("\nA table is available.")

#Ten= input("Give me a number, anyone number. ")
#Ten= int(Ten)

#if Ten %10==0:
    #print("\nThe number " + str(Ten) + " is a mulitple of ten.")
#else:
    #print("\nThe number " + str(Ten) + " is not a multiple of ten.")
#current_number= 10
#while current_number <=10:
    #current_number += 10
    #if current_number %10==0:
        #continue
   #print(current_number)




prompt = "\nTell me what topping you would like on your pizza?: "
print("I'll add, " + prompt + " to your pizza!")
prompt += "\n(Enter 'quit' to end the program.) "
message= ""
#while message != 'quit': #was for first problem
while True:
    topping= input(prompt)

    if topping == 'quit':
        break
    else: 
        print("I'll add, " + topping.title() + " to your pizza!")

#age = input("What is your age? ")
#age= int(age)
#if age <=3:
    #print("\nThe ticket is free. ")
#elif(age <=12):
    #print("The cost to your ticket is $10. ")
#else:
    #print("The cost to your ticket is $15. ")
#current_number= 1
#while current_number <=12:
    #print(current_number)
    #current_number +=12
