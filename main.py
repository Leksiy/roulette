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
        self.money = int(input('Начальная сумма (Enter = 5000 $)').strip() or '5000')

    def print_money(self):
        print(f'На счету: {self.money} $')

    def get_money(self):
        return self.money

class Game:
    def __init__(self):
        self.count_set = int(input('Количество попыток (Enter = 1000)').strip() or '1000')



if __name__ == '__main__':
    roulette = Roulette()
    gamer = Gamer()
    gamer.print_money()