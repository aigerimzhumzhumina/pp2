def reversesentence():
    sentence = input()
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
reversed_sentence = reversesentence()
print(reversed_sentence)