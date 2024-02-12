import random
def guessthenumber():
    secretnum = random.randint(1,20)
    print("Hello! What is your name?")
    name = input()
    print(name)
    print(f"Well, {name}, I am thinking of a number between 1 and 20")
    guess_num = 0
    while True:
        print("Take a guess")
        num = int(input())
        guess_num += 1
        if num < secretnum:
            print("Your guess is too low")
        elif num > secretnum:
            print("Your guess is too high")
        else:
            print(f"Good job, {name}! You guessed my number in {guess_num} guesses!")
guessthenumber()

