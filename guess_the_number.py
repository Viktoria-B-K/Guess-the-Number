import random
the_number = random.randint(1, 100)

while True:
    player_number = input('Guess the number (1-100): ')
    if not player_number.isdigit():
        print('Your input is not a number. Try again.')
        continue
    else:
        player_number = int(player_number)
        if 1 > player_number or player_number > 100:
            print('Your number is not in range from 1 to 100. Try again.')
            continue
        if player_number == the_number:
            print('Good job! You guessed the number!')
            break
        elif player_number < the_number:
            print('Too low!')
        elif player_number > the_number:
            print('Too high!')