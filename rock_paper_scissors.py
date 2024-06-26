import random

rock: str = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper: str = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors: str = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images: list[str] = [rock, paper, scissors]


def play_game() -> None:

    print("\nWelcome to rock paper scissors game\n")

    user_choice: int = int(input("Enter 0 for rock, 1 for paper, 2 for scissors : \n"))
    computer_choice: int = random.randint(0, 2)

    print('Computer has chosen :')
    print(game_images[computer_choice])

    if user_choice < 0 or user_choice > 2:
        print('You typed an invalid number (You Lose!)\n')
    else:
        print('You chose : ')
        print(game_images[user_choice])

        if user_choice == computer_choice:
            print('(It\'s A Draw!)\n')
        elif computer_choice == 0 and user_choice == 2:
            print("(You Lose!)\n")
        elif user_choice == 0 and computer_choice == 2:
            print('(You Win!)\n')
        elif user_choice > computer_choice:
            print('(You Win!)\n')
        elif computer_choice > user_choice:
            print('(You Lose!)\n')


def main() -> None:
    while True:
        play_game()
        end: str = input('Press (enter) to play another round or "N" to quit! : ').lower()
        if end == 'n':
            break
        else:
            continue


if __name__ == '__main__':
    main()
