# Let's play Stone_Scissor_Paper
# To work on this project we need to import random module 
 
import random

def gameWin(comp, you): 
     # If you choose same as the Comp then it will be tie!
    if comp == you:
        return None
    # Let's take a comp to define the cases
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you =="w":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True

print("Comp Turn: stone(s) scissor(w) or paper(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo ==3:
    comp = "g"
you = input("Your turn stone(s) scissor(w) or paper(g) ?")
print(f"Comp choise is : {comp}")
print(f"you choose is : {you}")

a = gameWin(comp, you)
if a == None:
    print("The game is a tie!")
elif a == False:
    print("You lose!")
elif a == True:
    print("You win!")

