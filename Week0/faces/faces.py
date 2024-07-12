def main():
    user_phrase = input("Enter a phrase: ")
    print(convert(user_phrase))

def convert(phrase):
    converted_phrase = phrase.replace(":)", "🙂").replace(":(", "🙁")
    return converted_phrase

main()
