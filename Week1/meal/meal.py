def main():
    time = input("What time is it? ")
    conv_time = convert(time)

    match conv_time:
        case conv_time if conv_time >= 7 and conv_time <= 8:
            print("breakfast time")
        case conv_time if conv_time >= 12 and conv_time <= 13:
            print("lunch time")
        case conv_time if conv_time >= 18 and conv_time <= 19:
            print("dinner time")


def convert(time):
    space_time = time.strip().split()

    if len(space_time) > 1:
        split_time = space_time[0].split(":")

        match space_time[-1]:
            case "a.m.":
                hours = float(split_time[0])
            case "p.m.":
                hours = float(split_time[0]) + 12
    else:
        split_time = time.split(":")

        hours = float(split_time[0])


    partial_hours = float(split_time[1]) / 60

    return hours + partial_hours


if __name__ == "__main__":
    main()
