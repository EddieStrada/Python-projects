import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
  global money
  #Tell the user his money amount
  print("Your current amount is: $" + str(money))
  if money < 0:
    print("You have insufficient funds :(")

  #compare bet with random number
  num = random.choice([1, 2])
  print(num)
  if guess == num:
    print("You win!")
    money += bet
  else:
    print("You lose! Better luck next time...")
    money -= bet

  #show result
  if num == 1:
    num = "Heads"
  else:
    num = "Tails"
  print("The result is: " + num + ".")
  print("You now have: $" + str(money) + ".")
#end of coin_flip



#Call your game of chance functions here
guess = int(input("Guess: 1 - Heads or 2 - Tails --> "))
bet = int(input("How much would you like to wager? --> "))
coin_flip(guess, bet)
print("$" + str(money))

