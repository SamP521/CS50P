inserted = 0
total_due = 50

while inserted < total_due:
    print(f"Amount Due: {total_due - inserted}")
    inserting = int(input("Insert Coin: "))

    match inserting:
        case 25:
            inserted += 25
        case 10:
            inserted += 10
        case 5:
            inserted += 5

print(f"Change Owed: {inserted - total_due}")
