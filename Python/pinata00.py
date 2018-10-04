import subprocess, os
word = '3'
while not word.isalpha():
    word = input("Enter your word of choice: ")
    if not word.isalpha():
        print("Not a valid word bud. Go ahead and try again.\n")
print("\n" * 50)

cls = os.system("CLS")

pinataCounter = 0
won = False
lettersGuessed = []

def printPinata(n):
    print("--+  ")
    pinataArr = ['  0\n','  |\n',' /', '|', '\\\n', '  |\n', ' /',' \\\n']
    if n != 3:
        pinataStr = ''
        for i in range(0,n):
            pinataStr += pinataArr[i]
        print(pinataStr)
    else:
        print('  0\n  |\n  |')
        
while not won and pinataCounter < 8:
    print('\n' * 3)
    printString = ' '
    for char in word:
        printString += (char + ' ') if char in lettersGuessed else ' _ '
    print(printString)
    guessLetter = 'haha'

    while len(guessLetter)!=1 or not guessLetter.isalpha() or guessLetter in lettersGuessed:
        guessLetter = input("Enter letter." + ("Already guessed this bub: " + ((str(lettersGuessed))[1:len(str(lettersGuessed))-1] + '\n') if len(lettersGuessed)>0 else '\n'))
        if len(guessLetter) !=1 or not guessLetter.isalpha():
            print("Not a letter. Try it again.\n")
        if guessLetter in lettersGuessed:
            print("Already guessed it. Ty again")

    lettersGuessed.append(guessLetter)
    won = True
    for char in word:
        if not char in lettersGuessed:
            won = False
    if guessLetter in word:
        print("Yay. Correct letter!\n")
    else:
        print("Not a letter in ze word")
        pinataCounter += 1
    if won or pinataCounter >=8:
        break
    print("Your pinata status: ")

    printPinata(pinataCounter)

if won:
    print("Good job lad! You correctly got " +word +'.\n')
else:
    print("You lose. You die")
printPinata(pinataCounter)
