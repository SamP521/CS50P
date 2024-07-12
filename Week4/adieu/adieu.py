import inflect

words = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)

print(f"Adieu, adieu, to {words.join(names)}")