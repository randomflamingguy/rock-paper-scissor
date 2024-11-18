import random
def getuserchoice():
    userchoice = str(input("Please enter your choice, (rock paper or scissor)")).lower()
    while userchoice not in ['rock', 'paper', 'scissor']:
        print("Invalid choice. Please enter rock paper or scissor")
        userchoice = str(input("Please enter your choice, (rock paper or scissor)")).lower()
    return userchoice
def getcomputerchoice():
    return random.choice(['rock', 'paper', 'scissor'])
def playgame():
    print("Welcome to rock paper scissor")
    userchoice = getuserchoice()
    comchoice = getcomputerchoice()
    print(f"You chose {userchoice}.")
    print(f"Computer choice: {comchoice}.")
    result = deterwin(userchoice, comchoice)
    print(result)
def deterwin(userchoice, comchoice):
    if userchoice == comchoice:
        return "It's a tie"
    elif(userchoice == 'rock' and comchoice == 'scissor') or \
        (userchoice == 'paper' and comchoice == 'rock') or \
        (userchoice == 'scissor' and comchoice == 'paper'):
        return "YOU WIN!"
    else:
        return "YOU LOSE!"
if __name__ == "__main__":
    playgame()