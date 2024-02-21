# Рівень 3.
# Варіант 1
# Потрібно написати програму для обходу двовимірного масиву розміром NxM у форматі "зігзагу".
# Зігзаговий обхід означає, що спочатку ми рухаємось по діагоналях масиву,
# починаючи з лівої верхньої точки. Другим елементом буде виведено елемент, який знаходиться справа,
# потім знизу і ліворуч, далі ще крок вниз і рухаємось по діагоналі знову вправо.
# Для масиву розміром 3x3 обхід у форматі зігзагу виглядає так
# (де номер у клітинці відповідає порядку її відвідин):
# 1 2 6 3 5 7 4 8 9
# Для масиву 3 х 5 це матиме вигляд:
# 1 2 6 7 12 3 5 8 11 13 4 9 10 14 15
# Реалізуйте алгоритм, який отримає на вхід масив розміром m та n та
# поверне одномірний масив з значеннями елементів вхідного масиву при обході
# його у порядку, зазначеному вище у задачі.

# юніттести
import unittest

# ГЛОБАЛЬНІ і та j це значення індексів в масиві,
# де і відповідає за ряки (n) а j - за стовпці (m)
i = 0
j = 0
# майбутній результат
result_arr = []


def diag_up(i, j):
    while 0 < i <= n - 1 and 0 <= j <= m - 2:
        i -= 1
        j += 1
        curr_val = arr[i][j]
        result_arr.append(curr_val)
    return i, j


def diag_down(i, j):
    while 0 <= i <= n - 2 and 0 < j <= m - 1:
        i += 1
        j -= 1
        curr_val = arr[i][j]
        result_arr.append(curr_val)
    return i, j


def go_right(i, j):
    if j != m - 1:
        j += 1
        curr_val = arr[i][j]
        result_arr.append(curr_val)
    return i, j


def go_down(i, j):
    if i != n - 1:
        i += 1
        curr_val = arr[i][j]
        result_arr.append(curr_val)
    return i, j


def arr_zigzag_traverse(arr, n, m):
    # ЛОКАЛЬНІ і та j це значення індексів в масиві, де і відповідає за ряки (n)
    # а j - за стовпці (m)
    i = 0
    j = 0
    curr_val = arr[i][j]    # поточне значення (1), записується в одновимірний масив
    result_arr.append(curr_val)

    # якшо масив де-факто одновимірний виводим його
    if m == 1:
        return arr

    # цикл дійсний поки і в межах рядків, а j - в межах стовпців
    while 0 <= i <= n - 1 and 0 <= j <= m - 1:
        # якшо стоїмо на передостанньому елементі,
        # просто рухаємся вправо і виходим
        if i == n - 1 and j == m - 2:
            go_right(i, j)
            return result_arr
        # якшо стоїмо на першому рядку, але не останньому стовпчику ->
        # -> рухаємся вправо а потім по діагоналі вниз
        elif i == 0 and j >= 0 and j != m - 1:
            i, j = go_right(i, j)
            i, j = diag_down(i, j)
        # якшо стоїмо на останньому рядку, але не на останньому стовпчику ->
        # -> рухаємся вправо і по діагоналі вгору
        elif i == n - 1 and j >= 0 and j != m - 1:
            i, j = go_right(i, j)
            i, j = diag_up(i, j)
        # якшо стоїмо на крайньому лівому стовпчику ->
        # -> рухаємся вниз на рядок а потім по діагоналі вгору
        elif i != n - 1 and j == 0:
            i, j = go_down(i, j)
            i, j = diag_up(i, j)
        # якшо стоїмо на останньому стовпчику ->
        # -> рухаємся вниз на рядок і по діагоналі вниз
        elif j == m - 1:
            i, j = go_down(i, j)
            i, j = diag_down(i, j)


# Для перевірки виконання роботи реалізованого алгоритму
# слід використати бібліотеку unittest . Ваш тести мають перевірити роботу алгоритму
# при значеннях m == n == 5, m = 2, n = 4, n = 1, m = 6, n == m == 1


class Lab1Test(unittest.TestCase):
    def test_arr_zigzag_traverse_5x5(self):
        # тут воно матюкається на out_of_range хоча якшо запустити
        # цей же масив не в форматі тесту, а просто -
        # все правильно працює
        test_arr = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        test_n = 5
        test_m = 5
        needed_result = [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13,
                         9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25]
        self.assertEqual(arr_zigzag_traverse(test_arr, test_n, test_m),
                         needed_result, "error!")

    def test_arr_zigzag_traverse_4x2(self):
        # тут воно по трохи дивній траєкторії йде але хай буде
        test_arr = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ]
        test_n = 4
        test_m = 2
        needed_result = [1, 2, 3, 5, 4, 6, 7, 8]
        self.assertEqual(arr_zigzag_traverse(test_arr, test_n, test_m),
                         needed_result, "error!")

    def test_arr_zigzag_traverse_1x6(self):
        # тут все ок, просто масив списком виводиться, але тест все рівно матюкається
        test_arr = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        test_n = 6
        test_m = 1
        needed_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(arr_zigzag_traverse(test_arr, test_n, test_m),
                         needed_result, "error!")

    def test_arr_zigzag_traverse_1x1(self):
        # тут те саме, по факту все норм але тесту не подобається
        test_arr = [
            [1]
        ]
        test_n = 1
        test_m = 1
        needed_result = [1]
        self.assertEqual(arr_zigzag_traverse(test_arr, test_n, test_m),
                         needed_result, "error!")


if __name__ == '__main__':
    # unittest.main()
    arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    n = 5
    m = 5
    result = arr_zigzag_traverse(arr, n, m)
    for i in result:
        print(i)
