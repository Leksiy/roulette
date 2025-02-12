from random import randint
from colorama import Fore as color

class Roulette:
    def __init__(self):
        self.COLOR = ['red', 'black']

    def round(self):
        result = randint(0, 1)
        return [self.COLOR[result], result]

class Gamer:
    def __init__(self):
        self.COUNT_SET = int(input('Количество попыток (Enter = 1000) ').strip() or '1000')
        self.money = int(input('Начальная сумма (Enter = 5000 $) ').strip() or '5000')

    def print_money(self):
        print(f'На счету: {self.money} $')

    def get_money(self):
        return self.money

class Game:
    def __init__(self):
        self.COUNT_REDOUBLE = int(input('Количество удвоений (Enter = 1000) ').strip() or '8')
        self.round = 1

    def game_new(self):
        self.round = 1

    def game_start(self, gamer):
        bet = pow(2, self.round - 1)
        if gamer.get_money() - bet < 0:
            self.end_game()

    def end_game(self):
        return True


if __name__ == '__main__':
    roulette = Roulette()
    gamer = Gamer()
    game = Game()
    for i in range(gamer.COUNT_SET):
        game.game_new()
        game.game_start(gamer)