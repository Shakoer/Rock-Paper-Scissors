import random

# Colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Game variables
moves = ["rock", "paper", "scissors"]
outcomes = {
    ("rock", "scissors"): "win",
    ("rock", "paper"): "lose",
    ("paper", "rock"): "win",
    ("paper", "scissors"): "lose",
    ("scissors", "paper"): "win",
    ("scissors", "rock"): "lose",
}

player_score = 0
computer_score = 0

while True:
    player = input("choose rock, paper or scissors: ").lower()
    if player not in moves:
        print(f"{RED}Invalid choice!{RESET}")
        continue

    computer = random.choice(moves)
    print(f"Computer chose: {computer}")

    if player == computer:
        result = "draw"
        print(f"{YELLOW}draw{RESET}")
    else:
        result = outcomes.get((player, computer))
        if result == "win":
            player_score += 1
            print(f"{GREEN}win!{RESET}")
        else:
            computer_score += 1
            print(f"{RED}lose{RESET}")

    print(f"{CYAN}Score - You: {player_score} | Computer: {computer_score}{RESET}")

    if input(f"{CYAN}play again? [y]: {RESET}") != "y":
        break