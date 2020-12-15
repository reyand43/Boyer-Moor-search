import numpy as np
import random
import string
from termcolor import colored, cprint
import time

result = []
text = []
def forming_d(pattern):
    """ Формируем массив d."""
    d = [len(pattern) for i in range(256)] #заполняем массив числами длины паттерна
    new_p = pattern[::-1] #создаем новый массив в виде развернутого паттерна
       
    for i in range(len(new_p)):
         
        if d[ord(new_p[i])] != len(new_p):
            continue           
        elif i!=0:
            d[ord(new_p[i])] = i
    return d
 
 
def search(string, pattern):
    """ Поиск Бойера - Мура."""
    start_time = time.time()
    d = forming_d(pattern)
    # x - начало прохода по string
    # j - проход по pattern
    # k - проход по string
    # s - количество совпавших символов
    len_p = x = j = k = len(pattern)
    s = 0
    while x<=len(string) and s<(len(pattern)):
        
        if pattern[j - 1] == string[k - 1]:
            ''' РАСКОММЕНТИРОВАТЬ, ЕСЛИ НЕОБХОДИМО ПОСМОТРЕТЬ СРАВНЕНИЕ СЛОВ'''
            #print(string[k - 1], '==', pattern[j - 1])
            j -= 1
            k -= 1
            s +=1
            
        else: 
            ''' РАСКОММЕНТИРОВАТЬ, ЕСЛИ НЕОБХОДИМО ПОСМОТРЕТЬ СРАВНЕНИЕ СЛОВ'''
            #print(string[k - 1], '!=', pattern[j - 1])
            d1=max(d[ord(string[k - 1])]-s, 1)
            d2=len(pattern)-1-pattern.find(string[x - 1])
            if (s == 0):
                shift = d1
            else:
                shift = max(d1, d2)
            x+=shift
            k = x
            j = len(pattern)
            
            s=0
        ''' РАСКОММЕНТИРОВАТЬ, ЕСЛИ НЕОБХОДИМО ПОСМОТРЕТЬ СРАВНЕНИЕ СЛОВ'''
        # print(string)
        # spaces = ''
        
        # for i in range(k-len(pattern)+s):
        #     spaces+= ' '
        # spaces+=pattern
        # print(spaces)
    j = 0
    # for i in range(len(string)):
    #     if (i==k+j and j<len(pattern)): 
    #         cprint(string[i], 'white', 'on_blue', end='')
    #         j+=1
    #     else:
    #         print(string[i], end='')
    res_time = (time.time() - start_time)*1000
    result.append(res_time)
    if s == len(pattern):
        print("Нашли. Время выполнения равно", res_time)
        print("")
    else:
        print("Не нашли!")
        
 

if __name__ == "__main__":
    words = "./dict.txt"
    WORDS = open(words).read().splitlines()
    #изменения количества слов
    interval = 800
    for i in range(20):
        arr = np.array([random.randint(0, 25486) for i in range(random.randint(interval, interval))])
        x = 0
        string = ''
        stringArr = []
        for a in arr:
            string =  WORDS[a] + ' ' + string
            stringArr.append(WORDS[a])
            x += 1
        # print('ИССЛЕДУЕМАЯ СТРОКА:', string)
        # patternNumber = random.randint(0, len(stringArr)-1)
        patternNumber = 0
        pattern = stringArr[patternNumber]
        #print('Длина строки', len(string))
        text.append(len(string))
        # print('')
        # print('ИСКОМАЯ ПОДСТРОКА:', pattern)
        search(string, pattern) 
    print('средняя длина текста равна', np.mean(text))
    print('средняя время выполнения', np.mean(result))
    
    

