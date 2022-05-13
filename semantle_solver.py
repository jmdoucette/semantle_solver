import math


def cosine_similarity(A,B):
    dot_product = sum([a * b for a,b in zip(A,B)])
    A_norm = math.sqrt(sum([a**2 for a in A]))
    B_norm = math.sqrt(sum([b**2 for b in B]))
    cosine_value = dot_product / (A_norm * B_norm)
    return cosine_value * 100


with open('word_list.txt', 'r') as file:
    candidates = []
    for line in file.read().splitlines():
        word, vector_string = line.split(',', maxsplit=1)
        vector = []
        for float_string in vector_string[1:-1].split(','):
            vector.append(float(float_string))

        candidates.append([word, vector])

guess_word, guess_vector = candidates[0]
print(f'all {len(candidates)} words are still candidates. guess: \"{guess_word}\"')

while len(candidates) > 1:
    similarity = float(input("enter similarity:").strip())
    new_candidates = []

    for word,vector in candidates:
        if abs(cosine_similarity(guess_vector, vector) - similarity) < .02:
            new_candidates.append([word, vector])

    candidates = new_candidates
    guess_word, guess_vector = candidates[0]

    print(f'there are {len(candidates)} words left. guess: \"{guess_word}\"')
        


    

    