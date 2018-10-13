letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = []
#Creates a list where each letter has a coresponding number value
letters_to_points = {letters:points for letters, points in zip(letters,points)}
letters_to_points[""] = 0

def score_word(word):
  point_total = 0
  #Take each letter in the input word and reference it to the list from before
  for i in range(len(word)):
    point_total += letters_to_points.get(word[i].upper(),0)
  return point_total

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "TENNIS", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

def update_point_totals():
  player_to_points = {}
  for player, words in player_to_words.items():
    player_points = 0
    #For a specific player, take their words played, run them through score_word and calculate their total points
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points

#Add a word to the list of words "player" has already played
def play_word(player, word):
  player_to_words[player].append(word)

print(update_point_totals())  
play_word("player1", "pepper")    
print(update_point_totals())
