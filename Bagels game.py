import random
def game():
    numbers=[str(digit)for digit in random.sample(range(0,10),3)]
    
    lives=0
    difficulty=input("Choose level(Easy,Medium,Hard)").lower()
    if difficulty=="easy":
        lives=19
    elif difficulty=="medium":
        lives=7
    elif difficulty=="hard":
        lives=2
    else:
        print("Invalid input")
        return
    while lives>0:
        guess=input("Guess any three numbers")
        if len(guess)!=3:
            print("Invalid your guess must be three numbers")
            continue
        Fermi=0
        Pico=0
        for i in range(3):
            if guess[i] == numbers[i]:
                print("Femi")
                Fermi +=1
            elif guess[i] in numbers[i]:
                print("Pico")
                Pico +=1
            elif guess[i] not in numbers[i]:
                print("Bagel")
        if Fermi==3:
            print("Congratulation you won")
            play_again=input("Do you wish to continue (yes or no)").lower()
            if play_again=="yes":
                game()
            else:
                print("Thanks for playing")
                return    
        lives -=1
        print(f"you have {lives} lives left")
    print("You lost,The three digits are", "".join(numbers))
    play_again=input("Do you wish to continue").lower()
    if play_again=="yes":
        game()
    else:
        print("Thankf for playing")
game()        
                
