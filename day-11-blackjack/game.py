from os import system
from cards import Card


def tally(cards):
    total = 0
    aces = 0
    for card in cards:
        total += card.value()
        if card.face == 'A':
            aces += 1
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


class Game:

    def __init__(self):
        self.over = False
        self.dealer = [Card(False), Card()]
        self.player = [Card(), Card()]
        self.message = 'Welcome to Blackjack!'

    def draw(self):
        system('clear')
        print(f'{self.message}\n')
        for hand in [self.dealer, self.player]:
            printout = [card.draw() for card in hand]
            total = [''] * 7
            total[3] = '= ' + (str(tally(hand)) if hand[0].shown else '?')
            printout.append(total)
            for i in range(7):
                print(' '.join([lines[i] for lines in printout]))
        print('')

    def end(self, message):
        self.message = message
        self.over = True

    def hit(self):
        self.player.append(Card())
        score = tally(self.player)
        if score == 21 and len(self.player) == 2:
            self.end('Blackjack! You win!')
        elif score > 21:
            self.end('Bust. You lose.')
        elif len(self.player) > 4:
            self.end('5-Card Charlie! You win!')

    def stand(self):

        # Time to reveal the dealer's face-down card.
        self.dealer[0].shown = True

        # Dealer hits on 16.
        while not self.over:
            score = tally(self.dealer)
            if score > 21:
                self.end('Dealer busts. You win!')
            elif len(self.dealer) > 4:
                self.end('Dealer has a 5-Card Charlie. You lose.')
            elif score > 16:
                if score < tally(self.player):
                    self.end('You win!')
                elif score > tally(self.player):
                    self.end('You lose.')
                else:
                    self.end('Dealer wins on a tie. You lose.')
            else:
                self.dealer.append(Card())
