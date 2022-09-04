############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 

from art import logo
print(logo)
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start():
  player = {
    "cards" : [],
    "status" : True,
    "card1" : random.choice(cards),
    "card2" : random.choice(cards),
    "sum" : 0,
    "black_jack" : False,
  }
  dealer = {
    "cards" : [],
    "status" : True,
    "card1" : random.choice(cards),
    "card2" : random.choice(cards),
    "sum" : 0,
    "black_jack" : False,
  }
 
  player["sum"] = player["card1"] + player["card2"]
  player["cards"].append(player["card1"])
  player["cards"].append(player["card2"])
  dealer["sum"] = dealer["card1"] + dealer["card2"]
  dealer["cards"].append(dealer["card1"])
  dealer["cards"].append(dealer["card2"])
  

  print(f'Your cards:{player["card1"]}, {player["card2"]}, current score: {player["sum"]}\nDealer\'s first card is: {dealer["card1"]}')

  if player["sum"] == 21:
    player["black_jack"] = True
  if dealer["sum"] == 21:
    player["black_jack"] = True

  if player["sum"] > 21 :
    if player["card1"] == cards[0] or player["card2"] == cards[0]:
      player["sum"] -= 10
    else:
      print("You lose")
      

  give_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
  while give_another_card == "y":
    player["sum"] = another_round(player["sum"], player["cards"])
    player["status"] = above21(player["sum"], player["cards"])
    print(f"Your cards: {player['cards']}, current score: {player['sum']}")
    if player["status"] == False:
      # compare(player, dealer)
      break
    else:
      give_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      
  while dealer["sum"] < 17 :
    # print(f"Dealers current score: {dealer['sum']}")
    dealer["sum"] = another_round(dealer["sum"], dealer["cards"])
    print(f"Dealers current score: {dealer['sum']}")
    dealer["status"] = above21(dealer["sum"], dealer["cards"])
    if dealer["status"] == "False":
      # compare(player, dealer)
      break
    
  compare(player, dealer)
  play_again = input("Do you want to play again? y/n\n")
  if play_again == "y":
    start()
    
  
def compare(player, dealer):
  print(f"Player score: {player['sum']}, Dealer score: {dealer['sum']}")
  if player["sum"] == dealer["sum"]:
    print("Draw")
  elif player["black_jack"] == True:
    print("You win!")
  elif dealer["black_jack"] == True:
    print("You lose")
  elif player["status"] == False:
    print("You lose")
  elif dealer["status"] == False:
    print("You win")
  elif player["sum"] > dealer["sum"] :
    print("You win!")
  else:
    print("You lose")
    
      
    
def above21(sum, own_cards):
  if sum > 21:
    for card in own_cards:
      if card == cards[0]:
        sum -= card
        card = 1
        sum += 1
        return True
      else:
        return False
  else:
    return True

def another_round(sum, own_cards):
  another_card = random.choice(cards)
  own_cards.append(another_card)
  sum += another_card
  return sum

  
start()

# print(result)
# if result == True:
#   print("You win")