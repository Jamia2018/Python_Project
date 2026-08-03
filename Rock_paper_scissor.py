
    # """
    # WORKFLOW OF PROJECT:
    # 1- Input from the user(Rock,Paper,Scissor)
    # 2- Computer choice (Computer will choose randomly not condionally)
    # 3- Result print
    
    # Case:
    # A- Rock
    # Rock-Rock = tie
    # Rock-Paper = Paper win
    # Rock-Scissor = Rock win
    
    # B-Paper
    # Paper-Paper = tie
    # Paper-Rock = Paper win
    # Paper-Scissor = Scissor win
    
    # C-Scissor
    # Scissor-Scissor = tie
    # Scissor-Rock = Rock win
    # Scissor-paper = Scissor win
import random

# List of possible moves
item_list = ["Rock", "Paper", "Scissor"]

# User input
user_choice = input("Enter your move (Rock, Paper, Scissor): ")

# Computer chooses randomly
com_choice = random.choice(item_list)

# Show choices
print(f"\nUser choice = {user_choice}")
print(f"Computer choice = {com_choice}\n")

# Decide winner
if user_choice == com_choice:
    print("🤝 Match Tie!")

elif user_choice == "Rock":
    if com_choice == "Paper":
        print("📄 Paper covers Rock. Computer wins!")
    else:
        print("🪨 Rock smashes Scissor. You win!")

elif user_choice == "Paper":
    if com_choice == "Rock":
        print("📄 Paper covers Rock. You win!")
    else:
        print("✂️ Scissor cuts Paper. Computer wins!")

elif user_choice == "Scissor":
    if com_choice == "Paper":
        print("✂️ Scissor cuts Paper. You win!")
    else:
        print("🪨 Rock smashes Scissor. Computer wins!")

else:
    print("❌ Invalid input! Please enter Rock, Paper, or Scissor.")