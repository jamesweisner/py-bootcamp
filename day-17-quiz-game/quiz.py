from random import getrandbits
from math import sqrt


def fibonacci(n):
    a, b = (0, 1)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return b


def is_prime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True


class Quiz:

    def __init__(self):
        self.score = 0
        self.index = 0
        self.questions = []

        types = [
            'prime number',
            'perfect square',
            'triangle number',
            'Fibonacci number',
        ]

        for _ in range(10):

            # Find a number where the highest place value digit is:
            #   - Even when the answer is true
            #   - Odd when the answer is false
            answer = bool(getrandbits(1))
            type = getrandbits(2)
            while True:
                n = self.get_number(type, answer)
                if (int(str(n)[0]) % 2 == 0) == answer:
                    break

            self.questions.append((f'{n} is a {types[type]}.', answer))

    def get_number(self, type, answer):

        # Prime numbers.
        if type == 0:
            while True:
                n = 1000 + getrandbits(16)
                n += 1 if (n % 2 == 0) else 0  # No even numbers.
                if is_prime(n) == answer:
                    return n

        # Perfect squares.
        elif type == 1:
            n = 100 + getrandbits(12)
            return (n * n) + (2 if not answer else 0)

        # Triangle number.
        elif type == 2:
            n = 1000 + getrandbits(16)
            return (n * (n + 1) // 2) + (1 if not answer else 0)

        # Fibonacci numbers.
        else:
            n = 3 + getrandbits(6)
            return fibonacci(n) + (1 if not answer else 0)

    def still_has_questions(self):
        return self.index < len(self.questions)

    def prompt(self, question):
        while True:
            guess = input(f"{self.index}. {question} [T/F] ").strip().lower()
            print('')
            if 'true'.startswith(guess):
                return True
            if 'false'.startswith(guess):
                return False

    def next_question(self):
        question, answer = self.questions[self.index]
        self.index += 1
        guess = self.prompt(question)
        if guess == answer:
            self.score += 1
            return True
        return False
