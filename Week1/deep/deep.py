answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
adjusted_answer = answer.lower().replace("-", " ").strip()

match adjusted_answer:
    case "42":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")
