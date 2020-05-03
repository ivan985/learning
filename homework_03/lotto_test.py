import pytest
from lotto import Card, Bag

# проверяет количество полей в создаваемой карточке
def test_card_len():
    players_card = Card('player')
    assert len(players_card.card_item) == 27

# проверяет, что все числа в карточке различны
def test_card_random():
    players_card = Card('player')
    # соберём все числа в один массив
    card_nums = []
    for i in players_card.card_item:
        if i != '_':
            card_nums.append(i)
    # сверим длинну массива чисел и их множества (при переводе в множество повторы удалятся и длина уменьшится)
    assert len(card_nums) == len(set(card_nums))

# проверим количество чисел в карточке
def test_card_numbers_number():
    players_card = Card('player')
    # соберём все числа в один массив
    card_nums = []
    for i in players_card.card_item:
        if i != '_':
            card_nums.append(i)
    assert len(card_nums) == 15

# проверим, что удовлетворяется требование сортировки чисел по возрастанию внутри одной строки карточки
def test_card_numbers_line_ascending():
    players_card = Card('player')
    # соберём все числа в один массив
    card_nums = []
    for i in players_card.card_item:
        if i != '_':
            card_nums.append(i)
    # выделим массивы для каждой строчки карточки
    mas_1 = card_nums[0:5]
    mas_2 = card_nums[5:10]
    mas_3 = card_nums[10:15]

    # сверим, что массив для каждой строчки отсортирован
    assert [mas_1, mas_2, mas_3] == [sorted(mas_1), sorted(mas_2), sorted(mas_3)]

# проверяет количество бочонков в мешке
def test_bag_len():
    bag_for_game = Bag()
    assert len(bag_for_game.bag) == 90

# проверяет, что все бочонки в мешке различны
def test_bag_random():
    bag_for_game = Bag()
    assert len(bag_for_game.bag) == len(set(bag_for_game.bag))