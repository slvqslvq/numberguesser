import json
from rich import print
from random import randrange
def main():

    print("[bold green]Добро пожаловать в числовую угадайку[/bold green]!")
    history = []
    while True:
        try:
            border = int(input("До какого числа будем загадывать? "))
        except ValueError:
            print("Введите лучше число")
            continue
        if is_border_valid(border):
            game_number = get_next_game_number(history)
            result = play_game(border,game_number)
            history.append(result)
        else:
            print("Неверная граница, начинаем заново")
            continue
        if not get_ask():
            print("Спасибо что сыграли, еще увидимся...")
            show_history(history)
            save_history(history)
            break
def play_game(border,games):

    number = randrange(1, border + 1)
    tries = 0
    while True:
        try:
            guess = int(input(f"Введите число от 1 до {border} \n"))
        except ValueError:
            print("Нужно ввести число")
            continue
        if is_valid(guess, border):
            tries += 1
            if guess < number:
                print("Ваше число меньше загаданного, попробуйте еще раз ")
            elif guess > number:
                print("Ваше число больше загаданного, попробуйте еще раз ")
            else:
                print(f"Вы угадали число за {tries} попыток, поздравляем!")
                return {
                    "games" : games,
                    "tries" : tries,
                    "number" : number,
                    "border" : border
                }
        else:
            print(f"Введите лучше число от 1 до {border}")

def get_ask():
    print("Хотите сыграть еще разок? Y - да, N - нет")
    choice = input()
    return choice.lower() == "y"
        
def is_valid(guess, border):

    return 1 <= guess <= border

def is_border_valid(border):

    return border > 1

def show_history(history):
    print("История игр:")
    print()
    for game in history:
        print(f"Игра №{game['games']}")
        print()
        print(f"Количество попыток : {game['tries']}")
        print(f"Загаданное число : {game['number']}")
        print(f"Граница 1-{game['border']}")
        print()

def get_next_game_number(history):
    return len(history) + 1

def save_history(history):
    with open ("history.json", "w") as file:
        json.dump(history,file)

main()

