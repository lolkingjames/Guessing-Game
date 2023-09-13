import random


def game():
    print('Welcome to guess the number!')
    print('To stop anytime, enter: q')
    score = 0
    a = input('Guess a number')
    while True:
        if a == "q":
            print(f"Game over")
            print(f'Final Score = {score}')
            break
        else:
            x = int(a)
            score = score
            rand = random.randint(1, 10)
            if x == rand:
                score += 10
                print('Great Guess!')
                print(f'Score: {score}')
                a = input('Guess a number')
            else:
                print(rand)
                print(f'Score: {score}')
                a = input('Guess a number')


game()