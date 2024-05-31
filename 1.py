import random
from collections import Counter

source_word = "ЛИНГВИСТИКА"

def get_new_bilba_word_rule1(source_word=source_word, symbols_qty=5):
    result = ""
    alphabet = list(set(source_word))
    for i in range(symbols_qty):
        sym = random.choice(alphabet)
        result += sym
        alphabet.remove(sym)
    return result

def get_new_bolba_word(source_word=source_word, symbols_qty=5):
    result = ""
    ndict = { key: value for key, value in Counter(source_word).most_common() }
    alphabet = list(set(source_word))
    vowels = ["А","И"]
    for pos in range(1,symbols_qty+1):
        if pos in [2,4]:
            sym = random.choice(vowels)
        else:
            sym = random.choice(alphabet)
        ndict[sym] = ndict[sym] - 1
        if ndict[sym] == 0:
            alphabet.remove(sym)
            if sym in vowels:
                vowels.remove(sym)
        result += sym
    return result

get_new_bilba_word_rule2 = get_new_bolba_word

def play_rule_1():
    attempts = 0
    while True:
        attempts += 1
        w1 = get_new_bilba_word_rule1()
        w2 = get_new_bolba_word()
        if w1 == w2:
            return attempts

def count_prob_rule1(n=100):
    lst = []
    for _ in range(n):
        lst.append(1/play_rule_1())
    return sum(lst)/len(lst)

def play_rule_2():
    attempts = 0
    while True:
        attempts += 1
        w1 = get_new_bilba_word_rule2()
        w2 = get_new_bolba_word()
        if w1 == w2:
            return attempts

def count_prob_rule2(n=100):
    lst = []
    for _ in range(n):
        lst.append(1/play_rule_2())
    return sum(lst)/len(lst)


count1 = count_prob_rule1(n=100)
print(count1)
count2 = count_prob_rule2(n=100)
print(count1)