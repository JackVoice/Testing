statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

def graduation_mailer(credits,gpa):
  if gpa >= 2 or credits >= 120:
    return True

print(graduation_mailer(100,3))
print(graduation_mailer(120,1.9))
print(graduation_mailer(100,1.5))
