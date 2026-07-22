import json
def load_history():
    try:
        with open ("history.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_history(history):
    with open ("history.json", "w") as file:
        json.dump(history,file)


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