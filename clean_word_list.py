import random
import gensim

with open('word_list_raw.txt', 'r') as file:
    word_list_raw = file.read().splitlines()
    random.shuffle(word_list_raw)

pretrained_embeddings_path = "GoogleNews-vectors-negative300.bin"
word2vec = gensim.models.KeyedVectors.load_word2vec_format(pretrained_embeddings_path, binary=True)

with open('word_list.txt', 'w') as file:
    for raw_word in word_list_raw:
        start = raw_word.index('\"') + 1
        end = raw_word.rindex('\"')
        word = raw_word[start:end]

        vector = list(word2vec[word])
        file.write(word + ',' + str(vector) + '\n')



