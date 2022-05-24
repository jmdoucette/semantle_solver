from semantle_solver import read_word_vector, cosine_similarity


with open('word_list.txt', 'r') as file:
    candidates = list(map(read_word_vector, file.read().splitlines()))

guess_avgs = []
for i,(guess_word, guess_vector) in enumerate(candidates):
    print(f'iteration {i}')

    similarity_count = {}
    for answer_word,answer_vector in candidates:
        similarity = round(cosine_similarity(guess_vector, answer_vector) * 10000)
        if similarity not in similarity_count:
            similarity_count[similarity] = 1
        else:
            similarity_count[similarity] += 1

    guess_sum = 0
    for answer_word,answer_vector in candidates:
        similarity = round(cosine_similarity(guess_vector, answer_vector) * 10000)
        guess_sum += 1 / similarity_count[similarity]
    guess_avgs.append(guess_sum / len(candidates))

with open('guess_avgs.txt', 'w') as file:
    for (word, _), guess_avg in zip(candidates, guess_avgs):
        file.write(word + ',' + str(guess_avg) + '\n')










