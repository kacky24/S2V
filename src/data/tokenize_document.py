from nltkjp import word_tokenize


def main():
    fr = open('sample_corpus_jp_short.txt', 'r')
    fw = open('tokenized.txt', 'w')

    for line in fr.readlines():
        words = word_tokenize(
                    line.strip(), True, ['動詞', '名詞', '形容詞'])
        st = ' '.join(words)
        fw.write(st + '\n')
    fw.close()
    fr.close()


if __name__ == '__main__':
    main()
