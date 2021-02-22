import time
from colorama import Fore
import random
print("GAME THEORY")
time.sleep(2)
print("In this simulation, you get to play against popular game theory characters. You can either 'Cooperate' or 'Defect'. Type in the serial number to play against a particular character.")
time.sleep(1)
print("Each will get 2 points if both cooperate. If both defect, both earn no points. If one defects and the other cooperates, the one who defects gets 3 points, while the other gets -1 points.")
print("Here are the available characters:")
print(Fore.BLUE + "1. COPYCAT: Hello! I start with Cooperate, and afterwards, I just copy whatever you did in the last round. Meow")
print(Fore.YELLOW + "2. GRUDGER: Listen, pardner. I'll start cooperatin', and keep cooperatin', but if y'all ever cheat me, I'LL CHEAT YOU BACK 'TIL THE END OF TARNATION.")
print(Fore.WHITE + "3. ALWAYS CHEAT: the strong shall eat the weak")
print(Fore.MAGENTA + "4. ALWAYS COOPERATE: Let's be best friends! <3")
print(Fore.GREEN + "5. DETECTIVE: First: I analyze you. I start: Cooperate, Cheat, Cooperate, Cooperate. If you cheat back, I'll act like " + Fore.BLUE + "Copycat" + Fore.GREEN + ". If you never cheat back, I'll act like " + Fore.WHITE + "Always Cheat" + Fore.GREEN + ", to exploit you. Elementary, my dear Watson.")
print(Fore.CYAN + "6. COPYKITTEN: Hello! I'm like " + Fore.BLUE+ "Copycat" + Fore.CYAN + ", except I Cheat back only after you Cheat me twice in a row. After all, the first one could be a mistake! Purrrrr")
print(Fore.GREEN + "7. SIMPLETON: hi i try start cooperate. if you cooperate back, i do same thing as last move, even if it mistake. if you cheat back, i do opposite thing as last move, even if it mistake.")
print(Fore.RED + "8. RANDOM: Monkey robot! Ninja pizza tacos! lol i'm so random (Just plays Cheat or Cooperate randomly with a 50/50 chance)")
options = ["c", "d"]
orgnoofrounds = int(input(Fore.RESET + "Enter the number of rounds you want to play: "))
character = int(input("Enter the serial number of the opposing character: "))
noofrounds = orgnoofrounds
playerpoints = 0
mypoints = 0
prevpinput = "a"
allpinputs = []
prevmychoice = "a"
def pointchecker(pchoice, mchoice):
	if pchoice == "d" and mchoice == "c":
		return(3, -1)
	if pchoice and mchoice == "c":
		return(2, 2)
	if pchoice == "c" and mchoice == "d":
		return(-1, 3)
	if pchoice and mchoice == "d":
		return(0, 0)
if character == 1:
	while noofrounds != 0:
		if noofrounds == orgnoofrounds:
			mychoice = "c"
		else:
			mychoice = prevpinput
		pinput = input("Enter 'C' to Cooperate and 'D' to Defect: ")
		pinput = pinput.lower()
		while pinput not in options:
			pinput = input("Only enter 'C' or 'D': ")
			pinput = pinput.lower()
		prevpinput = pinput
		if mychoice == "c":
			print("The Copycat cooperated!")
		else:
			print("The Copycat defected!")
		a, b = pointchecker(pinput, mychoice)
		playerpoints += a
		mypoints += b
		print(f"You have {playerpoints} points!")
		print(f"The Copycat has {mypoints} points!")
		noofrounds += -1
if character == 2:
	while noofrounds != 0:
		if noofrounds == orgnoofrounds:
			mychoice = "c"
		else:
			if "d" not in allpinputs:
				mychoice = "c"
			if "d" in allpinputs:
				mychoice = "d"
		pinput = input("Enter 'C' to Cooperate and 'D' to Defect: ")
		pinput = pinput.lower()
		while pinput not in options:
			pinput = input("Only enter 'C' or 'D': ")
			pinput = pinput.lower()
		allpinputs.append(pinput)
		if mychoice == "c":
			print("The Grudger cooperated!")
		else:
			print("The Grudger defected!")
		a, b = pointchecker(pinput, mychoice)
		playerpoints += a
		mypoints += b
		print(f"You have {playerpoints} points!")
		print(f"The Grudger has {mypoints} points!")
		noofrounds += -1
if character == 3:
	while noofrounds != 0:
		mychoice = "d"
		pinput = input("Enter 'C' to Cooperate and 'D' to Defect: ")
		pinput = pinput.lower()
		while pinput not in options:
			pinput = input("Only enter 'C' or 'D': ")
			pinput = pinput.lower()
		print("Always Cheat has Defected!")
		a, b = pointchecker(pinput, mychoice)
		playerpoints += a
		mypoints += b
		print(f"You have {playerpoints} points!")
		print(f"Always Cheat has {mypoints} points!")
		noofrounds += -1
if character == 4:
	while noofrounds != 0:
		mychoice = "c"
		pinput = input("Enter 'C' to Cooperate and 'D' to Defect: ")
		pinput = pinput.lower()
		while pinput not in options:
			pinput = input("Only enter 'C' or 'D': ")
			pinput = pinput.lower()
		print("Always Cooperate has Cooperated!")
		a, b = pointchecker(pinput, mychoice)
		playerpoints += a
		mypoints += b
		print(f"You have {playerpoints} points!")
		print(f"Always Cooperate has {mypoints} points!")
		noofrounds += -1
if character == 5:
	while noofrounds != 0:
		if noofrounds == orgnoofrounds or noofrounds == orgnoofrounds - 2 or noofrounds == orgnoofrounds - 3:
			mychoice = "c"
		if noofrounds == orgnoofrounds - 1:
			mychoice = "d"
		pinput = input("Enter 'C' to Cooperate and 'D' to Defect: ")
		pinput = pinput.lower()
		while pinput not in options:
			pinput = input("Only enter 'C' or 'D': ")
			pinput = pinput.lower()
		if noofrounds == orgnoofrounds or noofrounds == orgnoofrounds - 1 or noofrounds == orgnoofrounds - 2 or noofrounds == orgnoofrounds - 3:
			allpinputs.append(pinput)
		if noofrounds < orgnoofrounds -3:
			if "d" in allpinputs:
				if noofrounds == orgnoofrounds - 4:
					mychoice = "c"
				else:
					mychoice = prevpinput
			if "d" not in allpinputs:
				mychoice = "d"
		prevpinput = pinput
		if mychoice == "c":
			print("The Detective cooperated!")
		else:
			print("The Detective defected!")
		a, b = pointchecker(pinput, mychoice)
		playerpoints += a
		mypoints += b
		print(f"You have {playerpoints} points!")
		print(f"The Detective has {mypoints} points!")
		noofrounds += -1
if character == 6:
	while noofrounds != 0:
		if noofrounds == orgnoofrounds:
			mychoice = "c"
		else:
			if "c" not in allpinputs and len(allpinputs) == 2:
				mychoice = "d"
			if "c" in allpinputs and len(allpinputs) == 2:
				mychoice = "c"
		pinput = input("Enter 'C' to Cooperate and 'D' to Defect: ")
		pinput = pinput.lower()
		while pinput not in options:
			pinput = input("Only enter 'C' or 'D': ")
			pinput = pinput.lower()
		allpinputs.append(pinput)
		i = allpinputs[0]
		if len(allpinputs) > 2:
			allpinputs.remove(i)
		if mychoice == "c":
			print("The Copykitten cooperated!")
		else:
			print("The Copykitten defected!")
		a, b = pointchecker(pinput, mychoice)
		playerpoints += a
		mypoints += b
		print(f"You have {playerpoints} points!")
		print(f"The Copykitten has {mypoints} points!")
		noofrounds += -1
if character == 7:
	while noofrounds != 0:
		if noofrounds == orgnoofrounds:
			mychoice = "c"
		else:
			if prevpinput == "c":
				mychoice = prevmychoice
			if prevpinput == "d":
				if prevmychoice == options[0]:
					mychoice = options[1]
				if prevmychoice == options[1]:
					mychoice = options[0]
		pinput = input("Enter 'C' to Cooperate and 'D' to Defect: ")
		pinput = pinput.lower()
		while pinput not in options:
			pinput = input("Only enter 'C' or 'D': ")
			pinput = pinput.lower()
		prevpinput = pinput
		prevmychoice = mychoice
		if mychoice == "c":
			print("Simpleton cooperated!")
		else:
			print("Simpleton defected!")
		a, b = pointchecker(pinput, mychoice)
		playerpoints += a
		mypoints += b
		print(f"You have {playerpoints} points!")
		print(f"Simpleton has {mypoints} points!")
		noofrounds += -1
if character == 8:
	while noofrounds != 0:
		mychoice = random.choice(options)
		pinput = input("Enter 'C' to Cooperate and 'D' to Defect: ")
		pinput = pinput.lower()
		while pinput not in options:
			pinput = input("Only enter 'C' or 'D': ")
			pinput = pinput.lower()
		if mychoice == "c":
			print("Random cooperated!")
		else:
			print("Random defected!")
		a, b = pointchecker(pinput, mychoice)
		playerpoints += a
		mypoints += b
		print(f"You have {playerpoints} points!")
		print(f"Random has {mypoints} points!")
		noofrounds += -1
characters = {1: "Copycat", 2: "Grudger", 3: "Always Cheat", 4: "Always Cooperate", 5: "Detective", 6: "Copykitten", 7: "Simpleton", 8: "Random"}
if playerpoints > mypoints:
	print("You have won!")
if mypoints > playerpoints:
	print(f"{characters[character]} has one!")