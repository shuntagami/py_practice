l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()

# lambaを使って上の2行を簡潔に書ける
sample_func = lambda word: word.capitalize()

# change_words(l, sample_func)

change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())
