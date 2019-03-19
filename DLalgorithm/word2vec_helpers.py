import multiprocessing
import numpy
from gensim.models import Word2Vec


def embedding_sentences(sentences, embedding_size=128, window=5, min_count=5, file_to_load = None, file_to_save=None):
    if file_to_load is not None:
        w2vModel = Word2Vec.load(file_to_load)
    else:
        w2vModel = Word2Vec(sentences, size=embedding_size, window=window, min_count=min_count,
                            workers=multiprocessing.cpu_count())
        if file_to_save is not None:
            w2vModel.save(file_to_save)
    all_vectors = []
    embedding_dim = w2vModel.vector_size
    embedding_unknown = [0 for i in range(embedding_dim)]
    for sentence in sentences:
        this_vector = []
        for word in sentence:
            if word in w2vModel.wv.vocab:
                this_vector.append(w2vModel[word])
            else:
                this_vector.append(embedding_unknown)
        all_vectors.append(this_vector)
    return all_vectors

# sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
# # model = Word2Vec(sentences, min_count=1)
# vectors = embedding_sentences(sentences)
#
# print(vectors)
# print(numpy.array(vectors).shape)
# say_vector = model['say']  # get vector for word
# print(say_vector)