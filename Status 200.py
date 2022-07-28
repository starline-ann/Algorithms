'''Задача:
Вам дан массив натуральных чисел ai. 
Найдите число таких пар элементов (ai, aj), где |ai-aj|%200 == 0 and i<j.

Решение через число сочетаний:
Пусть исходный массив numbers = [203, 404, 204, 200, 403]

Рассортируем все числа на подмассивы по признаку: одинаковый остаток от деления на 200.

sub_arr = [[200], [203, 403], [404, 204]]

Количество пар элементов = числу сочетаний из кол-ва чисел в подмассивах по 2.
'''

def get_number_of_good_pairs(numbers) -> int:
    N = 200
    # create 200 subarrays and add numbers with same remainder of the division by 200
    sub_arr = [[] * n for n in range(N)]
    for a in numbers:
        i = a % N
        sub_arr[i].append(a)
    
    # count number of combinations of elements in every subarray
    def combinations(n, k):
        # C(n, k) = n! / k! / (n-k)! = (n-k+1)(n-k+2)...(n) / k(k-1)(k-2)...1 
        comb = 1
        for i in range(n-k+1, n+1):
            comb *= i
        for i in range(1, k+1):
            comb /= i
        return int(comb)
    
    sum = 0
    for i in range(N):
        lenth = len(sub_arr[i])
        if lenth > 1:
            sum += combinations(lenth, 2)

    return sum

n = int(input())
numbers = list(map(int, input().split()))
print(get_number_of_good_pairs(numbers))
