def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    test = start_letters(plate) and length(plate) and numbers(plate) and punctuation(plate)
    return test


def start_letters(plate):
    if plate[0:2].isalpha():
        return True
    else:
        return False


def length(plate):
    if len(plate) >=2 and len(plate) <= 6:
        return True
    else:
        return False


def numbers(plate):
    num_ctr = 0
    idx = 0

    for char in plate:
        if char.isdigit():
            num_ctr += 1

            if not plate[-1].isdigit():
                return False

            if char == "0" and num_ctr == 1:
                return False

            if idx != len(plate) - 1:
                if not plate[idx + 1].isdigit():
                    return False
        idx += 1
        
    return True


def punctuation(plate):
    for char in plate:
        if not char.isalpha() and not char.isdigit():
            return False

    return True


main()