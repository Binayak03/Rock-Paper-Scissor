import os
from getpass import getpass

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Color codes
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

# Game Title
print(f"{GREEN}🎮  WILD  🪨 📄 ✂️  GAME{RESET}")
print(f"""{RESET}Select your move:
    {RED}R for ROCK 🪨
    {MAGENTA}P for PAPER 📄
    {BLUE}S for SCISSORS ✂️{RESET}
""")

# Hidden inputs
player1Move = getpass("Player1: Enter your MOVE (R/P/S): ").strip().upper()
player2Move = getpass("Player2: Enter your MOVE (R/P/S): ").strip().upper()

# Print a space between inputs and result
print("\n--- RESULT ---\n")

# Game Logic
if player1Move == "R":
    if player2Move == "R":
        print("It's a TIE! 😐")
    elif player2Move == "P":
        print("Player2 WINS! 📄 beats 🪨")
    elif player2Move == "S":
        print("Player1 WINS! 🪨 crushes ✂️")
    else:
        print(f"{RED}❌ Invalid move by Player2!{RESET}")

elif player1Move == "P":
    if player2Move == "P":
        print("It's a TIE! 😐")
    elif player2Move == "S":
        print("Player2 WINS! ✂️ cuts 📄")
    elif player2Move == "R":
        print("Player1 WINS! 📄 covers 🪨")
    else:
        print(f"{RED}❌ Invalid move by Player2!{RESET}")

elif player1Move == "S":
    if player2Move == "S":
        print("It's a TIE! 😐")
    elif player2Move == "R":
        print("Player2 WINS! 🪨 crushes ✂️")
    elif player2Move == "P":
        print("Player1 WINS! ✂️ cuts 📄")
    else:
        print(f"{RED}❌ Invalid move by Player2!{RESET}")

else:
    print(f"{RED}❌ Invalid move by Player1!{RESET}")
