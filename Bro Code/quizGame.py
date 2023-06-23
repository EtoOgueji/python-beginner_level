# create a skeletal structure
# fill in the blanks later

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i) # prints optionsQ1 to optionsQ4
        guess = input("Enter option: ").upper()

        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS:")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = correct_guesses/len(questions)

def play_again():
    pass

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

optionsQ1 = ["A. Guido Van Rossum", "B. Bill Gates", "C. Ryan Gosling", "D. Elon Musk"]

optionsQ2 = ["A. 1923", "B. 1991", "C. 1956", "D. 1995"]

optionsQ3 = ["A. SNL", "B. America's got talent", "C. Monty", "D. Chicken republic"]

optionsQ4 = ["A. Yes", "B. Sometimes", "C. Not fully", "D. Ask Your Daddy"]

options = [optionsQ1, optionsQ2, optionsQ3, optionsQ4] # or use a list of tuples

new_game()