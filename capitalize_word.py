quote = "I don't hate them...I just feel better when they're not around."
word = input("Dwse Leksi: ")
while word != "quit":
    word = word.lower()
    word = word.strip()
    x = quote.find(word)
    y = len(word)
    if word in quote:
        word = word.upper()
        print(word)
        for i in range(x):
            print(quote[i], end="")
        print(word, end="")
        for i in range(x+y, len(quote)):
            print(quote[i], end="")
        print("\n")
    word = input("Dwse Leksi: ")
