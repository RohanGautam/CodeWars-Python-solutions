def find_children(s):
    return ''.join([(letter+letter.lower()*s.count(letter.lower())) for letter in sorted(s) if letter.isupper()])
