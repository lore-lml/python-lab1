print("Inserisci una parola")
word = input()
length=len(word)
if length < 2:
    print("")
else:
    print(word[0] + word[1] + word[length - 2] + word[length - 1])