def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    floated_dollars = float(d.replace("$", ""))
    return floated_dollars


def percent_to_float(p):
    floated_percent = float(p.replace("%", ""))
    return floated_percent / 100


main()
