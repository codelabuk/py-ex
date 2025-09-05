
current_movies = {'The Grinch': '11:00am',
                  'Rudolph': '1:00pm',
                  'Frosty the Snowman': '2:00pm'}

print("We ate scheduling below movies:")

for key in current_movies:
    print(key)

movie = input('What movie would you like to now shotime for ?\n')
showtime = current_movies.get(movie)
print(showtime)

if showtime == None:
    print("Request movie isn't available")