from random import randint
from colorama import Fore as color_text

class Roulette:
    def __init__(self):
        self.COLOR = ['Red', 'Blue']

    def round(self):
        result = randint(0, 1)
        print(f'Цвет рулетки ', end='')
        match result:
            case 0:
                print(color_text.RED, f'Red ', end='')
            case 1:
                print(color_text.BLUE, f'Blue ', end='')
        print(color_text.RESET, end='')
        return [self.COLOR[result], result]

class Gamer:
    def __init__(self):
        self.BET_COLOR = 'Red'
        self.COUNT_SET = int(input('Количество попыток (Enter = 1000) ').strip() or '1000')
        self.money = int(input('Начальная сумма (Enter = 5000 $) ').strip() or '5000')

    def print_money(self):
        print(f'На счету: {self.money} $')

    def get_money(self):
        return self.money

class Game:
    def __init__(self):
        self.COUNT_REDOUBLE = int(input('Количество удвоений (Enter = 8) ').strip() or '8')
        self.round = 1

    def game_new(self):
        self.round = 1

    def game_set(self, gamer, roulette):
        bet = pow(2, self.round - 1)
        result = self.game_end(gamer, bet)
        if not result:
            print(f'Ставка: {bet} $ ', end='')
            color = roulette.round()
            if gamer.BET_COLOR == color[0]:
                gamer.money += bet
                print(f'Выигрыш ', end='')
                result = True
            else:
                gamer.money -= bet
                print(f'Проигрыш ', end='')
            print(f'На счету: ({gamer.money}) $')
        return result

    def game_end(self, gamer, bet):
        if gamer.get_money() - bet < 0:
            print(f'На счету недостаточно средств ({gamer.money} $)')
            result = True
        else:
            result = False
        return result


if __name__ == '__main__':
    roulette = Roulette()
    gamer = Gamer()
    game = Game()
    for i in range(gamer.COUNT_SET):
        if gamer.money == 0:
            break
        game.game_new()
        for j in range(game.COUNT_REDOUBLE):
            game_end = game.game_set(gamer, roulette)
            if not game_end:
                game.round = j + 2
            else:
                break
