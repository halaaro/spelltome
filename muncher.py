import math
import random

def _clamp(num, minval, maxval):
    if maxval > minval:
        return max(min(num, maxval), minval)*1.0
    else:
        return max(min(num, minval), maxval)*1.0

#muncher.py
VOWELS = ['a','e','i','o','u','y']

def munch(word, fraction=0.5, vowel_bias=0.5):

    _frac = _clamp(fraction, 0, 1)
    _vowel_bias = _clamp(vowel_bias, 0.01, .99)
    _const_bias = 1 - _vowel_bias
    
    # break apart into characters
    letters = [c for c in word]
    num_letters = len(letters)
    min_removed = 1 + math.floor(_frac*(num_letters-1))

    # remove half the letters
    removed = 0
    while removed < min_removed:
        rand_idx = random.randint(0, num_letters-1)
        if letters[rand_idx] == '_':
            continue
        
        bias = _vowel_bias if letters[rand_idx] in VOWELS else _const_bias
        if random.random() >= bias: continue

        letters[rand_idx] = '_'
        removed += 1

    return letters


if __name__ == '__main__':
    print(munch('hello'))