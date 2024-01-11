sports=['football', 'basketball', 'mma', 'baseball', 'boxing','track']
print(sports[0:3])

print(sports[-3])
print(sports[-3:])
print(sports[3])

my_anime= ['one piece', 'dbz', 'naruto', 'aot']
friend_anime= my_anime[:]
print("My favorite animes to watch are:")
print(my_anime)
print("\nMy friend favorite animes are:")
print(friend_anime)
my_anime.append('dbs')
friend_anime.append('opm')
print("My favorite animes to watch are:")
print(my_anime)
print("\nMy friend's favorite animes are:")
print(friend_anime)
for animes in my_anime:
    print("my favororite animes to watch are," + animes.title())
print("\t\n")
for animes in friend_anime:
    print("My friend favorite animes to watch are," + "",animes.title())
print("\t\n")
buffet= ('lasagna', 'spaghetti', 'mushrooms', 'taco', 'mac')
print('\t\n')
print(buffet)
print('\n')
print("original food:")
for food in buffet:
    print(food)
buffet= ("vegan chicken, fries")
print("\nUpgrade buffet:")
for food in buffet:
    print(food)
print(buffet)
for food in buffet:
    print(food)
print("\t\n")


my_list=['apple', 'banana', 'oats', 'blueberry', 'kale']

print(f'My favorite foods are {my_list [1]}s , a sliced {my_list[0]}, and {my_list[4]} chips.')

my_age= 17

print(f'My age is {my_age} and today is my solar return!')