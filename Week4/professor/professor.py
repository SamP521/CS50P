import random


def main():
    score = play_game()
    print(f"Score: {score}")


def play_game():
    score = 0
    question = 1
    level = int(get_level())

    while question <= 10:
        add_1 = generate_integer(level)
        add_2 = generate_integer(level)

        question_string = str(add_1) + " + " + str(add_2) + " = "
        correct = add_1 + add_2
        tries = 0

        while True:
            tries += 1

            if tries > 3:
                print(question_string, correct)
                break

            try:
                user_answer = int(input(question_string))

            except ValueError:
                continue

            else:
                if user_answer == correct:
                    score += 1
                    break
                else:
                    print("EEE")
                    continue

        question += 1

    return score


def get_level():
    level = None

    while not level in ["1", "2", "3"]:
        level = input("Level: ")

    return level


def generate_integer(level):

    if level not in [1, 2, 3]:
        raise ValueError
    elif level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
