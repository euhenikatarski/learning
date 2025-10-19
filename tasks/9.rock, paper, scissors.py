def rps(p1, p2):

    p1 = p1.lower()
    p2 = p2.lower()

    # Если одинаковый выбор → ничья
    if p1 == p2:
        return "Draw!"

    # Логика победителя
    rules = {
        "rock": "scissors",   # камень бьёт ножницы
        "scissors": "paper",  # ножницы бьют бумагу
        "paper": "rock"       # бумага бьёт камень
    }

    if rules[p1] == p2:
        return "Player 1"
    else:
        return "Player 2"

print(rps("rock", "rock"))   # → Player 1