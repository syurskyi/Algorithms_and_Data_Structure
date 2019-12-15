from vowels import strip_vowels, text


def test_strip_vowels_on_zen():
    output, number_replacements = strip_vowels(text)

    assert number_replacements == 262

    assert 'Th* Z*n *f Pyth*n, by T*m P*t*rs' in output
    assert 'B***t*f*l *s b*tt*r th*n *gly' in output
    assert 'N*m*sp*c*s *r* *n* h*nk*ng gr**t *d**' in output
    assert '*lth**gh pr*ct*c*l*ty b**ts p*r*ty.' in output


def test_strip_vowels_on_other_text():
    text = """Hello world!
              We hope that you are learning a lot of Python.
              Have fun with our Bites of Py.
              Keep calm and code in Python!
              Become a PyBites ninja!
              All the way"""

    output, number_replacements = strip_vowels(text)

    assert number_replacements == 46

    assert 'H*ll* w*rld!' in output
    assert 'H*v* f*n w*th **r B*t*s *f Py' in output
    assert 'B*c*m* * PyB*t*s n*nj*!' in output
    assert '*ll th* w*y' in output