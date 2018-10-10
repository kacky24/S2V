import MeCab


tagger = MeCab.Tagger('-Ochasen -d /usr/lib/mecab/dic/mecab-ipadic-neologd')
tagger.parse('')


def word_tokenize(doc, normal=False, inc_class=[]):
    '''
    word tokenizer
    doc -> word list
    normal: transform to base form or not
    inc_class: list that contains classes to be extracted
    '''
    res = tagger.parseToNode(doc)
    words = []
    if normal:
        while res:
            content = res.feature.split(',')
            word = content[6]
            clas = content[0]
            if clas in inc_class:
                words.append(word)
            res = res.next
    else:
        while res:
            word = res.surface
            clas = res.feature.split(',')[0]
            if clas in inc_class:
                words.append(word)
            res = res.next

    return words
