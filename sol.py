import numpy as np
import random
import string
from termcolor import colored, cprint

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
 
    d = forming_d(pattern)
    # x - начало прохода по string
    # j - проход по pattern
    # k - проход по string
    # s - количество совпавших символов
    len_p = x = j = k = len(pattern)
    # число смещений
    s = 0
    counter = 0
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
            counter += 1
            s=0
        ''' РАСКОММЕНТИРОВАТЬ, ЕСЛИ НЕОБХОДИМО ПОСМОТРЕТЬ СРАВНЕНИЕ СЛОВ'''
        # print(string)
        # spaces = ''
        
        # for i in range(k-len(pattern)+s):
        #     spaces+= ' '
        # spaces+=pattern
        # print(spaces)
    j = 0
    for i in range(len(string)):
        if (i==k+j and j<len(pattern)): 
            cprint(string[i], 'white', 'on_blue', end='')
            j+=1
        else:
            print(string[i], end='')
        
    print('')
    if s == len(pattern):
        return "Нашли. Число смещений равно %d." % counter
    else:
        return "Не нашли!"
 


arr = np.array([random.randint(0, 25487) for i in range(random.randint(50, 100))])
words = "./dict.txt"
WORDS = open(words).read().splitlines()

x = 0
string = ''
stringArr = []
for a in arr:
    string =  WORDS[a] + ' ' + string
    stringArr.append(WORDS[a])
    x += 1

print('ИССЛЕДУЕМАЯ СТРОКА:', string)
patternNumber = random.randint(0, len(stringArr)-1)
pattern = stringArr[patternNumber]
print('ИСКОМАЯ ПОДСТРОКА:', pattern)
print('')
print(search(string, pattern))


