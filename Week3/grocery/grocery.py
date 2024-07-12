grocery_list = []

while True:
    try:
        item = input()
    except EOFError:
        print("\n")
        break
    else:
        grocery_list.append(item.strip().upper())

grocery_set = set(grocery_list)
grocery_iter = list(grocery_set)
grocery_iter.sort()

for item in grocery_iter:
    counter = grocery_list.count(item)
    print(f"{counter} {item}")