def encodeWord(word, wordVocab):
    s = wordVocab.get(word)
    if s is not None:
        return [s]
    else:
        start, end = 0, 0
        s = None
        l = []
        while True:
            if end == 0:
                d = word[start:]
                o = wordVocab.get(d)
            else:
                d = word[start:end]
                o = wordVocab.get(d)
            if o is None:
                end -= 1
            else:
                l.append(o)
                start = end
                end = 0
                if start == 0:
                    break
        return l


def encode(j, wordVocab):
    l = []
    for x in j.split():
        l.extend(encodeWord(x, wordVocab))
    return l