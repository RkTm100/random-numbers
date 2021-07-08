import random
winner=random.randint(1,9)
chance=5



#if guess==winner:
 # print("You Win!!")
#elif guess != chance and chance>0:
 # print("Incorrect, try again! ")
  #guess=int(input("what is the number: "))
#else :
 # print("You lose.")

print("Number guessing game")
  
while chance<=5:
  guess=int(input("What is the number: "))

  if guess==winner:
    print("you Win")
    break
  elif guess!=winner and chance<=5 and guess<winner:
    print("Incorrect, try again. Guess a number higher than " + str(guess))
    chance=chance-1
  elif guess!=winner and chance<=5 and guess>winner:
    print("Incorrect, try again. Guess a number lower than " + str(guess))
    chance=chance-1

  else:
    print("You Lose!")
    