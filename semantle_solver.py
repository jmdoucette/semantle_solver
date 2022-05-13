import math


def cosine_similarity(vector_1,vector_2):
    """computes the cosine of the angle between vector_1 and vector_2"""
    dot_product = sum([a * b for a,b in zip(vector_1, vector_2)])
    vector_1_norm = math.sqrt(sum([a**2 for a in vector_1]))
    vector_2_norm = math.sqrt(sum([b**2 for b in vector_2]))
    return (dot_product / (vector_1_norm * vector_2_norm)) * 100



def read_word_vector(s):
    """from a string representing a word, vector pair returns the word, vector pair"""
    word, vector_string = s.split(',', maxsplit=1)
    vector = []
    for float_string in vector_string[1:-1].split(','):
        vector.append(float(float_string))
    return [word, vector]



def update_candidates(candidates, guess_vector, similarity):
    """given a list of the candidate words and """
    res = []
    for word, vector in candidates:
        if abs(cosine_similarity(guess_vector, vector) - similarity) < .02:
                res.append([word, vector])
    return res



def solve_from_user_input():
    with open('word_list.txt', 'r') as file:
        candidates = list(map(read_word_vector, file.read().splitlines()))

    while len(candidates) > 1:
        guess_word, guess_vector = candidates[0]
        print(f'{len(candidates)} words are still candidates. guess: \"{guess_word}\"')

        similarity = float(input("enter similarity:").strip())
        candidates = update_candidates(candidates, guess_vector, similarity)
        print([candidate[0] for candidate in candidates])

    if len(candidates) == 1:
        print(f'the secret word is \"{candidates[0]}\"')
    else:
        print('no words fit the entered creiteria')




solve_from_user_input()

    

    