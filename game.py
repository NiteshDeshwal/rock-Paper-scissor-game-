import random
print("winning rule of rock scissor paper are : \n"
      + "Rock  vs Paper : Paper wins!\n"
      +"Paper vs Scissor : Scissor wins!\n"
      +"Scissor vs Rock : Rock wins!")

while True:
    print("Enter choice : \n"
      +"1. Rock\n"
      +"2. Paper\n"
      +"3. Scissor")

    choice = int(input("Enter your choice : "))
    while choice>3 or choice <1:
        choice = int(input("Enter a valid Choice please."))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else :
        choice_name = 'Scissor'


    print("User choice is \n",choice_name)
    print("Now its computer turn....")


    comp_choice = random.randint(1,3)

    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else :
        comp_choice_name = "Scissor"

    print("computer choice is :\n",comp_choice_name)
    print("choice_name vs comp_choice_name")

    if choice == comp_choice:
        print("Its a draw",end="")
        result = "DRAW"


    if(choice == 1 and comp_choice == 2):
        print("Paper wins")
        result = 'Paper'
    elif(choice == 2 and comp_choice == 1):
        print("Paper wins")
        result = 'Paper'

    
    if(choice == 1 and comp_choice == 3):
        print("Rock wins")
        result = 'Rock'
    elif(choice == 3 and comp_choice == 1):
        print("Rock wins")
        result = 'Rock'
    

    if(choice == 2 and comp_choice == 3):
        print("Scissor wins")
        result = 'Scissor'
    elif(choice == 1 and comp_choice == 3):
        print("Scissor wins")
        result = 'Scissor'
     
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== user wins ==>")
    if result == comp_choice_name:
        print("<== compter wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing")