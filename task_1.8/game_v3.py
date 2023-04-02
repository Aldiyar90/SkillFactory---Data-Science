"""Игра угадай число
Компьютер сам загадывает список из 10000 чисел и сам угадывает число меньше чем за 20 попыток, 
затем выдает среднее количество попыток, за которое ему удалось угадать число.
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Компьютер угадывает число
    
    Args:
        number (int, number from list from score_game): Загаданное число из списка загаданных

    Returns:
        int: Число попыток
    """
    
    count = 0 # количсество попыток угадывания числа
    predict = np.random.randint(1, 101) # компьютер выдает предполагаемое число
        
    if predict == number: 
        count+=1 # если число угадано с первого раза - число попыток 1
    
    if predict > number: # если предполагаемое число больше загаданного определяем предполагаемое число через цикл
        True
        while predict != number:
            count += 1
            if predict > number: 
                predict //= 2 # если предполагаемое число больше делим на два, то тех пор пока предполагаемое число не станет меньше загаданного
            elif predict < number:
                while predict !=number: # когда предполагаемое число становится меньше загаданного создаем новый цикл
                    count += 1
                    if predict < number:
                        predict += 5 # прибавляем к предполагаемому числу 5 пока предполагаемое число не станет больше загаданного
                    elif predict > number:
                        predict -= 1 # отнимаем от предполагаемого числа 1 пока предполагаемое число не станет равным загаданному
                
    if predict < number: # если предполагаемое число меньше загаданного определяем предполагаемое число через цикл
        while predict != number:
            count += 1
            if predict < number:
                predict *= 2 # если предполагаемое число меньше умножаем на два, то тех пор пока предполагаемое число не станет больше загаданного
            if predict > 100:
                predict = 100 # если предполагаемое число больше 100, то приравниваем предполагаемое число к 100
            elif predict > number:
                while predict !=number: # содаем новыы цикл для уменьшения предполагаемого числа
                    count += 1
                    if predict > number:
                        predict -= 10 # уменьшаем предполагаемого на 10 пока предполагаемое число не станет меньше загаданного
                    elif predict < number:
                        predict += 1 # прибавляем к предполагаемому числу 1 пока предполагаемое число не станет равным загаданному
    
    return int(count) # итого число попыток


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=10000) # загадали список чисел
       
    for number in random_array: # определяем количесто попыток угадывания через функцию game_core_v3 и добавляем число попыток в лист count_ls
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls)) # находим среднее количесто попыток из листа count_ls
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score # возвращаем среднее количесто попыток угадывания числа
    
score_game(game_core_v3) 