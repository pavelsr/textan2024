import re
import nltk
import random
from nltk.corpus import words
nltk.data.path.append('words')
nltk.download('words', download_dir='words')
word_list = words.words()
words_five = [word.lower() for word in word_list if len(word) == 5]
guessed_word = random.choice(words_five)
print(guessed_word)

attempt_n = 1
checked_letters = []
while attempt_n <= 6:
    user_word = input()
    if len(user_word) > 5:
        print("Слово слишком длинное, попробуйте снова")
        continue
    if len(user_word) < 5:
        print("Слово слишком короткое, попробуйте снова")
        continue
    if not re.match(r'^[a-zA-Z]+$', user_word):
        print("Недопустимый символ в слове, попробуйте снова")
        continue

    print("Попытка %s" % (attempt_n))
    print("Ваше слово: %s" % (user_word) )
    if user_word == guessed_word:
        print("Поздравляем, вы выиграли")
        break
    
    for lu, lg in zip(user_word, guessed_word):
        if lu in checked_letters:
            continue
        elif lu == lg:
            print("%s стоит на правильном месте" % (lu) )
        elif lu in [ x for x in guessed_word ]:
            print("%s есть, но стоит не там" % (lu) )
        else:
            print("%s отсутствует в слове" % (lu) )
        checked_letters.append(lu)
    attempt_n += 1
print("К сожалению, вы проиграли. Загаданное слово: %s" % (guessed_word))
