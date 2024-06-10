from quiz import Quiz

quiz = Quiz()

print('Welcome to the evil math quiz!\n')
print(f'There are {len(quiz.questions)} questions.\n')

try:

    while quiz.still_has_questions():
        result = 'Correct!' if quiz.next_question() else 'Wrong...'
        score = f"Your score is: {quiz.score} / {quiz.index}"
        print(f"{result} {score}\n")

    print("You've completed the quiz!")

except KeyboardInterrupt:
    print('\n\nBye!\n')
