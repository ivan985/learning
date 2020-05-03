import random


# класс для карточки
class Card(object):
    def __init__(self, type):
        # генерируем 15 случайных номеров, которые будут содержаться в карточке
        card_nums = random.sample(range(1, 91), 15)

        # учитываем требование возрастания числел в каждой строке
        card_nums_line_1 = []
        card_nums_line_2 = []
        card_nums_line_3 = []
        for i in range(1,16):
            if 1 <= i <= 5:
                card_nums_line_1.append(card_nums[i-1])
            elif 6 <= i <= 10:
                card_nums_line_2.append(card_nums[i-1])
            elif 11 <= i <= 15:
                card_nums_line_3.append(card_nums[i-1])
        # получаем список из 15 чисел, остортированных внутри каждых 5
        card_nums_sorted = sorted(card_nums_line_1) + sorted(card_nums_line_2) + sorted(card_nums_line_3)

        # генериурем случайные позиции, на которых эти номера будут расположены
        card_line_nums = sorted(random.sample(range(1, 10), 5) +
                                random.sample(range(10, 19), 5) +
                                random.sample(range(19, 28), 5))

        # расставляем отсортированные числа по позициям, на выходе получая список
        card_list = []
        j = 0
        for i in range(1, 28):
            if i in card_line_nums:
                card_list.append(card_nums_sorted[j])
                j = j + 1
            else:
                card_list.append('_')

        # карточка, хранящаяся в виде списка
        self.card_item = card_list
        # тип карточки (игрок/компьютер)
        self.card_type = type
        # количество незачёркнутых чисел
        self.card_item_count = 15

    # печать карточки в наглядном виде
    def print_card(self):
        if self.card_type == 'player':
            print('------ Ваша карточка -----')
        elif self.card_type == 'computer':
            print('-- Карточка компьютера ---')

        str_for_print = ''
        for i in range(1, len(self.card_item) + 1):
            str_for_print = str_for_print + str(self.card_item[i-1]) + ' '
            if i % 9 == 0:
                print(str_for_print)
                str_for_print = ''
        print('--------------------------')

    # вычёркивание номера из карточки
    def change_card(self, num):
        for i in range (len(self.card_item)):
            if self.card_item[i] == num:
                self.card_item[i] = '--'
                self.card_item_count = self.card_item_count - 1


# класс для мешка для игры
class Bag (object):
    def __init__(self):
        self.bag = random.sample(range(1, 91), 90)


# функция для игры
def lotto_game():

    # задаются начальные данные для игры
    players_card = Card('player')
    computers_card = Card('computer')
    bag_for_game = Bag()
    step_num = 0

    # сама игра
    for barrel in bag_for_game.bag:

        # выводятся начальные данные для шага
        step_num = step_num + 1
        print('\nНовый бочонок: ' + str(barrel) + ' (в мешке осталось ' + str(90 - step_num) + ')')
        players_card.print_card()
        computers_card.print_card()

        # игрок и компьютер обрабатывают свои карточки
        answer = input('Зачеркнуть цифру? (y/n)')
        while answer not in ['y', 'n']:
            answer = input('Вы опечатались. Введите ответ в формате (y/n). Зачеркнуть цифру?')
        if answer == 'y':
            if barrel in players_card.card_item:
                players_card.change_card(barrel)
            else:
                print('Такой цифры на карточке нет. Вы проиграли.')
                break
        elif answer == 'n':
            if barrel in players_card.card_item:
                print('Цифра была на карточке. Вы проиграли.')
                break
        if barrel in computers_card.card_item:
            computers_card.change_card(barrel)

        # проверяется, не завершилась ли игра после обработки
        if computers_card.card_item_count == 0 and players_card.card_item_count == 0:
            print('\nНичья. Все карточки пусты:')
            players_card.print_card()
            computers_card.print_card()
            break
        elif computers_card.card_item_count == 0:
            print('\nВы проиграли. Карточка компьютера пуста:')
            players_card.print_card()
            computers_card.print_card()
            break
        elif players_card.card_item_count == 0:
            print('\nВы выиграли. Ваша карточка пуста:')
            players_card.print_card()
            computers_card.print_card()
            break


if __name__ == '__main__':
   lotto_game()

