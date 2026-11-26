import random

U = "\033[4m"
RESET = "\033[0m"
option: str = ""
machineOption: str = ""
you: int = 0
machine: int = 0
msg: str = ""

while option != "end":
    
    print(f"\n{U}R{RESET}ock\n{U}P{RESET}aper\n{U}S{RESET}cissors\n   {U}E{RESET}nd\n")

    option=input("Option: ").lower()
    machineOption = random.choice(["rock", "paper", "scissors"])

    match option:
        case "r": option = "rock"
        case "p": option = "paper"
        case "s": option = "scissors"
        case "e": option = "end"
    #    case _:      "case else. Must be the last case"
        
    if option == "end":
        msg = "End of game"
    elif option == machineOption:
        msg = f"Same option \"{option}\", repeating"
    elif option not in ["rock", "paper", "scissors"]:
        msg = f"❌ Invalid option \"{option}\", repeating"
    elif option == "rock" and machineOption == "scissors" or \
            option == "paper" and machineOption == "rock" or \
            option == "scissors" and machineOption == "paper":
        you += 1
        msg = f"✅ You win: \"{option}\" beats \"{machineOption}\""
    else:
        machine += 1
        msg = f"\nThe machine wins: \"{machineOption}\" beats \"{option}\""

    print(f"\n=============== You: {you} === Machine: {machine} ===========================")
    print(f"\n{msg}")