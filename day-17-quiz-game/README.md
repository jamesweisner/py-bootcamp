I made several noteworthy improvements to this capstone project:

* It's a math quiz!
* A hidden trick lets you impress your friends with a perfect score.
* A much cleaner user interface.

The quiz is 10 questions long and each question is of a random type:

1. Is this a prime number?
2. Is this a perfect square?
3. Is this a triangle number?
4. Is this a Fibonacci number?

Questions are randomized so that 50% of the time the answer is true.

The hidden trick is easy:

 * If the highest place value digit is *even*, the answer is *true*.
 * If the highest place value digit is *odd*, the answer is *false*.

The algorithm I wrote to accomplish this treachery is:

1. Randomly decide if we want the answer to be true or false.
2. Randomly decide which type of question to ask.
3. Get a random number where the answer would be true (e.g. a prime).
4. If the answer is supposed to be false, spoil it by adding one.
5. Repeat steps 3-4 until the highest place value digit lets you cheat.
