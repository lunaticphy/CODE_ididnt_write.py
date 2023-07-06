import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def code_generator():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code
def guess_code():

    while True:
        guess = input("Guess the code ").upper().split(" ") # what that split is gonna do EXP: " G G G G " -> ["G", "G", "G", "G"]

        if len(guess) != CODE_LENGTH:
            print(f"Invalid answer: <must be/ {CODE_LENGTH} long.")
            continue
         # now we need to make sure that all of the color in the guess are IN the COLORS (thus we use a for loop)
        for color in guess:
            if color not in COLORS:
                print(f"Invalid {color}")
                break
        else:
            break
    return guess
def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_count[guess_color] -= 1
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos += 1
            color_count[guess_color] -= 1

    return correct_pos, incorrect_pos
def game():
    print("Wlecome to some code you asically didnt write!!")
    print("The valid colors are", COLORS)
    code = code_generator()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print("YOU LOSE HOMIE")
            break

        print(f"correct position: {correct_pos} | Incorrect position: {incorrect_pos}")
    else:
        print("YOU ran out!!!!!!!!!!!!!!!!!!")

if __name__ == "__main__":
    game()
