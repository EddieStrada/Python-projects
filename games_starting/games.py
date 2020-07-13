import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
  global money
  #if user has no funds
  if money <= 0:
    print()
    print("Sorry, you have insufficient funds.")
  else:
    #Tell the user his money amount
    print("This is Coin Flip! Your current amount is: $" + str(money))
    if guess == 1:
      print("Your choice is: HEADS")
    else:
      print("Your choice is: TAILS")
    #ask if he wants to continue
    choice = input("Would you like to keep playing? (Y/N) - ")
    if choice.upper() == "Y":
      num = random.choice([1, 2])
      while money > 0:
        #compare bet with random number
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
        if money > 0:
          choice = input("Would you like to keep playing? (Y/N) - ")
          if choice.upper() == "Y":
            guess = int(input("Guess again: 1 - Heads or 2 - Tails --> "))
          else:
            print("Come again soon.")
            break
        else:
          print("You have insufficient funds.")
          break
    #if choice == N
    else:
      print("Come again soon.")
    print("You're going home with: $" + str(money) + ".")

#end of coin_flip

def cho_han(guess, bet):
  global money
  dice1 = random.choice(range(1,7))
  dice2 = random.choice(range(1,7))
  total = dice1 + dice2

  if guess.lower() == "even" and total % 2 == 0:
    print("You win! The total is Even.")
    money += bet
  elif guess.lower() == "odd" and total % 2 != 0:
    print("You win! The total is Odd.")
    money += bet
  elif guess.lower() == "even" and total % 2 != 0:
    print("You lose. The total is Odd.")
    money -= bet
  elif guess.lower() == "odd" and total % 2 == 0:
    print("You lose. The total is Even.")
    money -= bet

  print("Your total is $" + str(money) + ".")



#Call your game of chance functions here
# guess = int(input("Guess: 1 - Heads or 2 - Tails --> "))
# bet = int(input("How much would you like to wager? --> $"))
# coin_flip(guess, bet)

# print("$" + str(money))

guess = input("Guess: Odd or Even --> ")
bet = int(input("How much would you like to wager? --> $"))
cho_han(guess, bet)
