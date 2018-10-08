destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
  
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#Finds the index for a given destination inside destinations.
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  #Finds where traveler is going
  traveler_destination = traveler[1]
  #Relates where they are going to global index
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

attractions = []
#Creates a blank list of blank lists that corelate to the amount of destinations avaliable 
for i in destinations:
  attractions.append([])

def add_attraction(destination, attraction):
  try:
    #Figures out global index for destination
    destination_index = get_destination_index(destination)
    #Adds attraction to respective list for destination
    attractions_for_destination = attractions[destination_index].append(attraction)
  except ValueError:
    #For locations that aren't covered
    return

add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  #Finds global index for destination
  destination_index = get_destination_index(destination)
  #All relevant attractions in destination
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    #Define the current attraction being looked at
    possible_attraction = attraction
    #For the current attraction, get it's tags
    attraction_tags = attraction[1]
  
    for interest in interests:
      #If the interest of the user are located in the current tags of the current attraction
      if interest in attraction_tags:
        #Add it to the list we will show them
        attractions_with_interest.append(possible_attraction[0])
  #Return all relvant attractions
  return attractions_with_interest

#print(find_attractions("Los Angeles, USA", ['art']))

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  #Find all attractions that match the traveler with information provided
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  #Give them the information in a tidy way
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  for i in range(len(traveler_attractions)):
    #Check if last attraction or not to see if comma or full stop required
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += "the " + traveler_attractions[i] + "."
    else:
      interests_string += "the " + traveler_attractions[i] + ", "
  return interests_string

#print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))
