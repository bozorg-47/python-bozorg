def is_vowel(x):
    vowel = ["a","e","i","o","u","A","E","I","O","U"]
    if x in vowel:
        return True
    else:
        return False
print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel("E"))
print(is_vowel("Z"))