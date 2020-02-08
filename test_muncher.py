from muncher import munch

def count_chars(letters, char):
    return len([c for c in letters if c == char])

def test_muncher__returns_list():
    assert isinstance(munch('a'), list)

def test_muncher__always_munches_at_least_one_letter():
    assert count_chars(munch('a'), '_') > 0
    assert count_chars(munch('abc', fraction=0), '_') > 0
    assert count_chars(munch('abc', fraction=0.1), '_') > 0
    assert count_chars(munch('abc', fraction=-1), '_') > 0
    assert count_chars(munch('abc', fraction=10), '_') > 0

def test_muncher__honors_fraction():
    assert count_chars(munch('abc', fraction=0), '_') == 1
    assert count_chars(munch('abc', fraction=0.49), '_') == 1
    assert count_chars(munch('abc', fraction=0.50), '_') == 2
    assert count_chars(munch('abc', fraction=0.99), '_') == 2
    assert count_chars(munch('abc', fraction=1), '_') == 3

def test_muncher__honors_vowel_fraction():
    res1 = munch('abc', fraction=0, vowel_bias=1)
    assert count_chars(res1, '_') == 1
    assert res1[0] == '_'

    res2 = munch('abc', fraction=0, vowel_bias=0)
    assert count_chars(res2, '_') == 1
    assert res2[0] == 'a'

    res2 = munch('doo', fraction=0, vowel_bias=0)
    assert count_chars(res2, '_') == 1
    assert res2[0] == '_'

    res2 = munch('doo', fraction=0, vowel_bias=1)
    assert count_chars(res2, '_') == 1
    assert res2[0] == 'd'

    res2 = munch('doo', fraction=0.5, vowel_bias=1)
    assert count_chars(res2, '_') == 2
    assert res2[0] == 'd'

def test_muncher__resolves_invalid_bias():
    res2 = munch('doo', fraction=0.5, vowel_bias=0)
    assert count_chars(res2, '_') == 2
    assert res2[0] == '_'

    res2 = munch('you', fraction=0.5, vowel_bias=0)
    assert count_chars(res2, '_') == 2
