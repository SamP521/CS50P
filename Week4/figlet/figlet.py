from pyfiglet import Figlet, FigletFont
from random import choice
import sys


def main():
    font_list = FigletFont.getFonts()
    fig = Figlet()

    if len(sys.argv) == 1:
        fig.setFont(font=choice(font_list))

    elif len(sys.argv) == 3:
        if args_invalid(font_list):
            sys.exit("Incorrectly formatted arguments.")
        fig.setFont(font=sys.argv[2])

    else:
        sys.exit("Incorrect number of arguments.")

    phrase = input("Input: ")
    print("Output: \n")
    print(fig.renderText(phrase))


def args_invalid(font_list):
    return sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in font_list
