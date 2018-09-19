sentence = input("Type something elaborate: ")
theSentence = sentence.split(' ')
for word in theSentence:
    x = list(word)
    for char in x:
        print(char)
    print('-')

