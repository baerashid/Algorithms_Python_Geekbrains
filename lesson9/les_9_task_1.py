# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * задача считается решённой, если в коде использована функция вычисления хеша (hash(), sha1()
# или любая другая из модуля hashlib)

import hashlib

def find_substr(string) -> int:
    """
    Решать будем так
    1. выбрать подстроку
    2. искать подстроку такой же длины в оставшейся строке
    3. если нашли, то +1 и вносим хеш в таблицу, ибо такую же подстроку мы больше учитывать не будем
    :return: число вхождений
    """

    len_str = len(string)

    assert len_str>0, 'Пустая строка'

    uniques = 0
    hash_table = set()

    for i in range(len_str):
        for j in range(i+1,len_str+1):
            #excluse the string itself
            if not ((i == 0) & (j == len_str)):
                sub_sting = string[i:j]
                len_sub = len(sub_sting)
                h_sub = hashlib.sha1(sub_sting.encode('utf-8')).hexdigest()

                for k in range(len_str - len_sub + 1): # можно начинать не с нуля здесь а с i, ибо сзади вхождения точно посчитаны уже
                                                       # это уменьшит сложность, однако ж с нуля нагляднее
                    candidate = string[k:k + len_sub]
                    h_candidate = hashlib.sha1(candidate.encode('utf-8')).hexdigest()

                    # if hashes are the same and didnt encounter earlier
                    if (h_candidate == h_sub) &  ~(h_candidate in hash_table):
                        #print(sub_sting)
                        uniques += 1
                        hash_table.add(h_candidate)

    return uniques

string = input('Введите строку: ')
print(find_substr(string))

