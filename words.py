import collections
import random

len_dict = collections.defaultdict(list)
for word in open('engmix.txt'):
    word = word.rstrip('\n')
    len_dict[len(word)].append(word)

def of_length(length):
    return len_dict[length]

def random_word(min_len, max_len):
    word_bank = []
    for i in range(min_len, max_len):
        word_bank += of_length(i)
    if not word_bank:
        raise Exception('No words found! Please modify your range.')
    return random.choice(word_bank)
