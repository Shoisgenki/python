def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#--------------------------------------------------------


def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

#--------------------------------------------------------

def display_score(correct_guesses, guesses):
    print("----------------------")
    print("Results")
    print("----------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")

#--------------------------------------------------------


questions = {"Who created Python? : " : "A",
             "What year was Python created? : " : "B",
             "Python is tributed to which comedy group? : " : "C",
             "Art thou seeketh virtue amidst thee?" : "B"}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Soulja Boy", "D. Pau Gasol"],
           ["A. 1989", "B. 1991", "C. 2023", "D. 16th century"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. Pewdiepie"],
           ["A. True", "B. False", "C. Sometimes", "D. What?"]]

new_game()