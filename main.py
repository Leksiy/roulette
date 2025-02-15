from random import randint
from colorama import Fore as color_text

class Roulette:
    def __init__(self):
        """
        Объект класса Рулетка
        :return: None
        """
        super().__init__()
        self.COLOR = ['Red', 'Blue']
        self.color_current = 0

    def __str__(self):
        str = 'Цвет рулетки: '
        match self.color_current:
            case 0:
                str += color_text.RED + 'Red '
            case 1:
                str += color_text.BLUE + f'Blue '
        str += color_text.RESET
        return str

    def round(self):
        """
        Крутить рулетку. На какой цвет попал шарик?
        Код цвета: 0 - красный, 1 - голубой
        :return: [цвет, код цвета]
        :rtype: (str, int)
        """
        self.color_current = randint(0, 1)
        return [self.COLOR[self.color_current], self.color_current]

class Gamer:
    def __init__(self):
        """
        Объект класса Игрок
        :return: None
        """
        super().__init__()
        self.BET_COLOR = 'Red'
        self.LOSS_COUNT = 0
        self.SET_COUNT = int(input('Количество попыток (Enter = 1000): ').strip() or '1000')
        self.money = int(input('Начальная сумма (Enter = 5000 $): ').strip() or '5000')

    def __str__(self):
        str = f'На счету: {self.money} $. '
        return str

    def get_money(self):
        """
        Получить состояние счета
        :return: Количество денег на счету
        :rtype: int
        """
        return self.money

class Game:
    def __init__(self, roulette: Roulette, gamer: Gamer):
        """
        Объект класса Игра: roulette - рулетка, gamer - игрок
        :param roulette: Рулетка: Рулетка
        :param gamer: Игрок: Игрок
        :return: None
        """
        super().__init__()
        self.REDOUBLE_COUNT = int(input('Количество удвоений (Enter = 8): ').strip() or '8')
        self.round = 0
        self.set = 0
        self.bet = 0
        self.roulette = roulette
        self.gamer = gamer

    def __str__(self):
        str = f'Попытка: {self.set + 1}, '
        str += f'раунд: {self.round + 1}, '
        str += f'ставка: {self.bet} $. '
        return str

    def set_set_game(self):
        """
        Установка начальных значений перед новой попыткой
        :return: None
        """
        self.bet = 0
        self.round = 0

    def game_start(self):
        """
        Запуск игры
        :return: None
        """
        for self.set in range(self.gamer.SET_COUNT):
            self.set_set_game()
            if self.get_game_status():
                self.game_set()
            else:
                break
        self.game_end()

    def game_set(self):
        """
        Попытка игры
        :return: None
        """
        for self.round in range(self.REDOUBLE_COUNT):
            self.bet = pow(2, self.round)
            if self.get_game_status():
                if self.game_round():
                    break
            else:
                print(f'Недостаточно средств на счету для продолжения попытки. Начинаем новую попытку.')
                break

    def game_round(self):
        """
        Раунд игры
        :return: True - выигрыш, False - проигрыш
        :rtype: bool
        """
        print(self, end='')
        if self.gamer.BET_COLOR == self.roulette.round()[0]:
            self.gamer.money += self.bet
            result =  True
            str = color_text.RED + f'Выигрыш.  '
        else:
            self.gamer.money -= self.bet
            str = color_text.BLUE + f'Проигрыш. '
            result =  False
        str += color_text.RESET
        print(str, end='')
        print(self.gamer, end='')
        if not result and self.round == self.REDOUBLE_COUNT - 1:
            self.gamer.LOSS_COUNT += 1
            print(color_text.BLUE + f'Поражение', end='')
        print(color_text.RESET)
        return result

    def get_game_status(self):
        """
        Проверка окончания игры
        :return: True - игра продолжается, False - игра завершена
        :rtype: bool
        """
        result = True
        if self.gamer.money == 0:
            result = False
        if self.gamer.money - self.bet < 0:
            result = False
        return result

    def game_end(self):
        """
        Завершение игры
        :return: None
        """
        print(f'Игра завершена. ', end='')
        print(self.gamer, end='')
        print(f'Поражений: {self.gamer.LOSS_COUNT}')

if __name__ == '__main__':
    roulette = Roulette()
    gamer = Gamer()
    game = Game(roulette, gamer)
    game.game_start()
