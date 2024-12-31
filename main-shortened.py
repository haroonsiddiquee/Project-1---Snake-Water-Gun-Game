import random

'''

1  for snake
-1 for water
0  for gun

'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter Your Choice: ")
youDict = {"s":1, "w":-1, "g":0}
ReverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
you = youDict[youstr]

print(f"You Chose {ReverseDict[you]} \nComputer Chose {ReverseDict[computer]}")

if(computer == you):
    print("It's a Draw!")

else:

    '''
    
    if(computer == -1 and you == 1): (computer - you) = -2
        print("You Win!")

    elif(computer == -1 and you == 0): (computer - you) = -1
        print("You Lose!")

    elif(computer == 1 and you == -1): (computer - you) = 2
        print("You Lose!")

    elif(computer == 1 and you == 0): (computer - you) = 1
        print("You Win!")

    elif(computer == 0 and you == 1): (computer - you) = -1
        print("You Lose!")

    elif(computer == 0 and you == -1): (computer - you) = 1
        print("You Win!")

    else:
        print("Something went wrong!")
        
    The below logic is written on the basis of the value of the computer - you
    
    '''
    
    # This code is the short form of the code given above but it's readability is almost none.

    if((computer - you) == -1 or (computer - you) == 2 ):
        print("You Lose!")
    
    else:
        print("You Win!")
