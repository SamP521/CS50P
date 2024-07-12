camel = input("camelCase: ")
snake = []

for char in camel:
    if char.isupper():
        snake.append("_")
        snake.append(char.lower())
    else:
        snake.append(char)

print(f"snake_case: {"".join(snake)}")
