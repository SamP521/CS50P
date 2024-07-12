expression = input("Expression: ")
split_exp = expression.split()

val1 = float(split_exp[0])
val2 = float(split_exp[2])

match split_exp[1]:
    case "+":
        output = val1 + val2
    case "-":
        output = val1 - val2
    case "*":
        output = val1 * val2
    case "/":
        output = val1 / val2

print(round(output, 1))
