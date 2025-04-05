secret_word = input("введите слово для игры: ").strip().lower()
print("\033[2J")
win = False
all_letters = []
true_letters = []
points = [0, 0, 0]
counter = 0
while not win:

    letter = input(f"игрок {counter + 1} введите букву: ").strip().lower()
    if letter in all_letters:
        print('вы уже вводили эту букву')
    else:
        all_letters.append(letter)
        if letter in secret_word:
            print("вы угадали букву")
            true_letters.append(letter)
            points[counter] += 1
            print(F"ваши очки: {points[counter]}")
        else:
            print("такой буквы нет в слове")

    guessed_word = ""
    win = True
    for char in secret_word:
        if char in true_letters:
            guessed_word += char
        else:
            win = False
            guessed_word += "*"
    print(guessed_word)

    if win:
        print(f"""игрок 1: {points[0]}
игрок 2: {points[1]}
игрок 3: {points[2]}""")

    counter += 1
    if counter > 2:
        counter = 0






