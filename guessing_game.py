winning_number=20
print("this is a number guessing game.....")
input_number=int(input("guess your number between 1 to 100:"))
guess=1
game_over=False
while not game_over:
    if(winning_number==input_number):
        print(f"you win!,and you guess the number in{guess}time")
        game_over=True
    else:
        if(winning_number>input_number):
            print("you guess too low!")
            guess+=1
            input_number=int(input("guess again:"))
        else:
            print("you guess too high...!")
            guess+=1
            input_number=int(input("guess again"))        