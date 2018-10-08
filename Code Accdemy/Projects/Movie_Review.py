# Write your movie_review function here:
def movie_review(rating):
  message = "Avoid at all costs!"
  if rating >= 9:
    message = "Outstanding!"
  elif rating > 5:
    message = "This one was fun."
  return message
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."
