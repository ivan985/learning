'''
Лото

Правила игры.

Игра состоит из специальных карточек на которых отмечены числа и бочонков с цифрами

Всего 90 бочонков с цифрами от 1 до 90 (В жизни они обычно достаются из мешка чтобы можно было вытянуть случайно)

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Так выглядит пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер (*так же может быть 2 пользователя или 2 компьютера).
Каждому в начале выдается случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Компьютер всегда правильно зачеркивает свои цифры если они есть и продолжает если их нет

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода (как может выглядеть интерфейс игры):
- (знаком минус) отмечены уже зачеркнутые цифры

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

Подсказка: для написания программы удобно использовать ООП, примеры возможных классов: Игрок, Бочонок, Мешок, Карточка, ...
Так же можно придумать свою структуру классов либо воспользоваться процедурным программированием

'''

