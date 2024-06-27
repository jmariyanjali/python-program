import random
number = 0
for i in range(random.randint(45, 60)):
  number = number+1
  if number == 50:
    print("number reaches to 50")
    break
  else:
    print("number never reaches to 50")