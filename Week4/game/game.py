from random import randint


def main():
    level, target = get_level_target()
    play_game(level, target)


def get_level_target():
    while True:
        try:
            level = int(input("Level: "))
            target = randint(1, level)

            if level < 1:
                raise ValueError

        except ValueError:
            print("Level must be an integer greater than 1.")

        else:
            return level, target


def play_game(level, target):
    guess = None

    while guess != target:
        try:
            guess = int(input("Guess: "))

            if guess > level:
                raise ValueError

        except ValueError:
            print(f"Too large!")

        else:
            if guess == target:
                print("Just right!")
            elif guess > target:
                print("Too large!")
            elif guess < target:
                print("Too small!")


if __name__ == "__main__":
    main()
