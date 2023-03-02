def rev_sen(sen):
    words = sen.split()
    rev_words = [rev_word(word) for word in words]
    return " ".join(rev_words)

def rev_word(word):
    if len(word) == 1:
        return word
    else:
        return rev_word(word[1:]) + word[0]

string = input()
print(rev_sen(string))
