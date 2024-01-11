#def display_message():
    #"""Display a simple message"""
    #print("Hello folks, today I am learning about functions at the great program coding temple!")

#display_message()

#def favorite_book(book):
    #"""Display one favorite book"""
    #print("My favorite book is, " + book + "!")

#favorite_book('Rich dad, poor dad')

#def make_shirt(size_shirt, text_shirt):
    #"""Display the size of the shirt and the text on the shirt."""
    #print("\nThe size that I need is a " + size_shirt + ".")
    #print("My " + size_shirt + " message is " + text_shirt + ".")

#make_shirt('medium sized shirt', ' the metaverse')
#make_shirt(size_shirt= 'large sized shirt', text_shirt= 'AWOO')

#def make_shirt(text_shirt, size_shirt= 'large'):
   # """Display the size of the shirt and the text on the shirt."""
    #print("\nThe size that I need is a " + size_shirt + ".")
    #print("My " + size_shirt + " message is " + text_shirt + ".")
    
#make_shirt('I love Python')

#def make_shirt(text_shirt, size_shirt= 'medium'):
    #"""Display the size of the shirt and the text on the shirt."""
    #print("\nThe size that I need is a " + size_shirt + ".")
    #print("My " + size_shirt, "shirt" + " message is " + text_shirt + ".")
    
#make_shirt('I love coding')

#def make_shirt(text_shirt, size_shirt= 'xlarge'):
    #"""Display the size of the shirt and the text on the shirt."""
    #print("\nThe size that I need is a " + size_shirt + ".")
    #print("My " + size_shirt, "shirt" + " message is " + text_shirt + ".")
    
#make_shirt('KING OF CODING')

#def descibe_city(city_name, country_name= 'thailand'):
   #"""Display a city and its country"""
    #print(city_name, " is in " + country_name + ".")

#descibe_city('Phuket')
#descibe_city('Hat Yai')
#descibe_city('Philadelphia')

#def city_country(city_name, country_name):
    #"""Return a city and its country name, neatly formatted."""
    #c= city_name + ' ' + country_name
    #return c

#name = city_country('Deptford,','New Jersey')
#print(name)
#n= city_country('Phuket,' ,'Thailand')
#print(n)
#ci= city_country('Hat Yai,','Thailand')
#print(ci)

#def make_album(artist_name, album_title, tracks = ' '):
    #"""Return a dictionary of information about a artist and its album."""
    #artist= {'artist': artist_name, 'album': album_title}
    #if tracks:
        #artist['tracks'] = tracks
        #return artist



#a= make_album('MRG', 'Metaverse')
#print(a)
#m= make_album('Soulking', 'New World')
#print(m)
#b= make_album('JID', 'DiCaprio 2')
#print(b)
#me= make_album('Lil Baby', 'My Turn(Deluxe)', tracks= 22)
#print(me)

def make_album(artist_name, album_title):
    """Return a dictionary of information about a artist and its album."""
    artist= artist_name + ' ' + album_title
    return artist
    
while True:
        print("\nPlease tell me your artist name: ")
        print("(enter 'q' at any time to quit)")
        
        a_name= input("Artist name: ")
        if a_name == 'q':
            break

        a_title= input("Album Title: ")
        if a_title == 'q':
            break

        ar_name= make_album(a_name, a_title)
        print("\nHello, " + ar_name , "looking forward to your album koc.")



