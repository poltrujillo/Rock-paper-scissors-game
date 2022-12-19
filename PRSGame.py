import random

def get_choices():
  options = ["rock", "paper", "scissors"]
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  computer_choice = random.choice(options)

  choices = {
    "player": player_choice,
    "computer": computer_choice
  }
  return choices

def check_win(player, computer):
  print(f"You chose: {player}, and computer chose: {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."

  elif player == "paper":
    if computer == "scissors":
      return "Scissors covers paper! You lose."
    else:
      return "Paper smashes rock! You win!"

  elif player == "scissors":
    if computer == "paper":
      return "Scissors smashes paper! You win!"
    else:
      return "Rock cover scissors! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)