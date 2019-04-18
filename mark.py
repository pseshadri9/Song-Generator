import numpy as np
import os
def markfile(f):
    if f not in os.listdir():
        raise Exception("Cannot find file")
    with open(f, 'rb') as f:
        text = f.read()
    corpus = text.split()
    def makepairs(corp):
        for i in range(len(corp) - 1):
            yield (corpus[i], corpus[i + 1])
    pairs = makepairs(corpus)
    transitionMatrix = {}
    lengths = {}
    states = {}
    for x, y in pairs:
        if x in states.keys():
            if y in states[x]:
                index = states[x].index(y)
                transitionMatrix[x][index] += 1
                lengths[x] += 1
            else:
                states[x].append(y)
                transitionMatrix[x].append(1)
                lengths[x] += 1
        else:
            states[x] = [y]
            transitionMatrix[x] = [1]
            lengths[x] = 1
    for key, value in transitionMatrix.items():
        transitionMatrix[key] = [float(x) / lengths[key] for x in value]
    return tuple([states, transitionMatrix])

def gensentence(f):
    model = markfile(f)
    print(model[0].keys())
    word = np.random.choice([*model[0].keys()])
    punc = ['.', '!', '?']
    while word.islower() == word and word not in punc:
        word = np.random.choice([*model[0].keys()])
    sentence = word.decode('UTF-8')
    count = 1
    while word not in punc and count < 50:
        word = np.random.choice(model[0][word], p=model[1][word])
       # print(word)
        sentence += ' ' + word.decode('UTF-8')
        count += 1
    return sentence

def gensentencefromword(f, word):
    model = markfile(f)
    num = np.random.choice(range(10, 25))
    sentence = word.decode('UTF-8')
    for x in range(num):
        word = np.random.choice(model[0][word], p=model[1][word])
        sentence += ' ' + word.decode('UTF-8')
    return sentence






