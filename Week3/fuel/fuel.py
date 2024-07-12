while True:
    try:
        fraction = input("Fraction: ")
        split_fraction = fraction.split("/")
        x = int(split_fraction[0])
        y = int(split_fraction[1])
        percent = x / y * 100

    except ValueError:
        print("Enter integers!")
    except ZeroDivisionError:
        print("The second number can't be zero!")

    else:
        if x > y:
            print("The first number can't be bigger than the second!")
            continue
        else:
            break

match percent:
    case percent if percent >= 99:
        print("F")
    case percent if percent <= 1:
        print("E")
    case _:
        print(f"{int(round(percent))}%")