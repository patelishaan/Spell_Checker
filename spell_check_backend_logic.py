import re
from tqdm import tqdm
import pickle
import pandas as pd
import os
if os.path.getsize('sherlock.pkl') > 0:
    with open('sherlock.pkl', 'rb') as f:
        word_prob = pickle.load(f)
        print('loaded successfuly')
else:
    print("File is empty.")

def split(word):
    parts = []
    for i in range(len(word) + 1):
        parts += [(word[ : i], word[i : ])]
    return parts


def delete(word):
    output = []
    for l, r in split(word):
        output.append(l + r[1:])
    return output


print(delete('loave'))


def swap(word):
    output = []
    for l, r in split(word):
        if (len(r) > 1):
            output.append(l + r[1] + r[0] + r[2:])
    return output


#print(swap('lvoe'))


def replace(word):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    output = []

    for l, r in split(word):
        for char in characters:
            output.append(l + char + r[1:])
    return output

def insert(word):

    characters = 'abcdefghijklmnopqrstuvwxyz'
    output = []

    for l,r in split(word):
        for char in characters:
            output.append(l + char + r)

    return output

def edit(word):
    return list(set(insert(word) + delete(word) + swap(word) + replace(word)))


def spell_check_edit_1(word, count=5):
    output = []
    suggested_words = edit(word)

    for wrd in suggested_words:
        if wrd in word_prob.keys():
            output.append([wrd, word_prob[wrd]])

    return (list(pd.DataFrame(output, columns=['word', 'prob']).sort_values(by='prob', ascending=False).head(count)['word'].values))


print(spell_check_edit_1('famili'))
def spell_check_edit_2(word, count=5):
    output=[]#two time correction
    suggested_word =edit(word)#one level edit
    for e1 in edit(word):
        suggested_word += edit(e1)#second level edit
    suggested_word = list(set(suggested_word))

    for wrd in suggested_word:
        if wrd in word_prob.keys():
            output.append([wrd,word_prob[wrd]])
    return list(pd.DataFrame(output, columns=['word', 'prob']).sort_values(by='prob', ascending=False).head(count)['word'].values)
#print(spell_check_edit_2('famili'))
