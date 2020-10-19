import random, copy, time

class LotoGame:
    def __init__(self, player1, player2):
        self.firstplayer = player1
        self.secondplayer = player2
        self.all_numbers = 90
        self.numbers_in_card = 15
        self.numbers_in_line = 5

    def card_generator(self):
        num_comb = random.sample(range(1, self.all_numbers + 1), self.numbers_in_card)
        card = [sorted(num_comb[i:i + self.numbers_in_line]) for i in range(0, len(num_comb), self.numbers_in_line)]
        return card

    def gen_barr_list(self):
        return random.sample(range(1, self.all_numbers + 1), 90)

    def get_barrel(self, barr_list):
        return barr_list.pop()

    def show_card(self, card):
        card = copy.deepcopy(card)  # чтобы числа в карточке не изменялись при игре
        placeholders = ' '.join(['{:>2}' for i in range(9)])  # создаём 9 ячеек в строке, разделённых пробелами
        for line in card:
            for space in ' ' * 4:
                line.insert(random.randint(0, len(line) - 1), space)  # заполняем пробелами произвольные 4 ячейки в строке
        return [placeholders.format(*line) for line in card]

    def update_card(self, card, barrel):  # вычёркиваем выпавшие числа из карточки
        for line in card:
            yield ['-' if x == barrel else x for x in line]

    def is_empty(self, card):
        for line in card:
            for elem in line:
                if elem != '-':
                    return False
        return True

    def barr_in_card(self, card, barrel):
        return barrel in [barrel for line in card for barrel in line]

    def start(self):
        print('Добро пожаловать в игру "Лото"!')
        time.sleep(1)
        print('Вы играете против компьютера.')
        time.sleep(1)
        print('Неверный ответ = проигрыш.')
        time.sleep(2)
        print('Составляются карточки (по 15 чисел в каждой)...')
        time.sleep(3)
        print('Выбирается случайный бочонок с числом от 1 до 90...')
        time.sleep(3)
        print('\nПоехали!\n')
        time.sleep(1)
        player_card, comp_card = self.card_generator(), self.card_generator()
        barrels = self.gen_barr_list()
        while True:  # пока не закроем все числа в карточке
            next_barrel = self.get_barrel(barrels)
            print(f'Новый бочонок: {next_barrel}. Осталось: {len(barrels)}')#.format(next_barrel, len(barrels)##))
            time.sleep(1)
            print('{0} Ваша карточка {0}\n{1}\n{2}\n{3}\n{4}'.format('-' * 6, *self.show_card(player_card), '-' * 27))
            print('{0} Карточка компьютера {0}\n{1}\n{2}\n{3}\n{4}'.format('-' * 3, *self.show_card(comp_card), '-' * 27))
            answer = 'a'
            while answer not in 'ynq':
                answer = input('Есть ли выпавшее число в вашей карточке? Нажмите y/n (= да/нет) или q для выхода из игры: ')
            if answer == 'q':
                break
            elif (answer == 'y' and self.barr_in_card(player_card, next_barrel)) or (
                    answer == 'n' and not self.barr_in_card(player_card, next_barrel)):
                print('Верно!\nСледующий ход...')
            else:
                print('Вы проиграли!')
                break
            player_card = list(self.update_card(player_card, next_barrel))
            comp_card = list(self.update_card(comp_card, next_barrel))
            if self.is_empty(player_card):
                print('Поздравляю! Вы закрыли все числа в своей карточке!')
                break
            if self.is_empty(comp_card):
                print('Компьютер закрыл все числа в своей карточке!')
                break

game = LotoGame('human_player', 'comp_player')
game.start()