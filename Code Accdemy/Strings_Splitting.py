authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

author_last_names = []
for i in range(len(author_names)):
  temp = []
  temp += author_names[i].split()
  author_last_names.append(temp[-1])

print(author_last_names)
