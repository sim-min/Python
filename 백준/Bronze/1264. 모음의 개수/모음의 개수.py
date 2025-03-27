while True:
    word = input()
    if word == "#":
        break
    print(word.count("a") + word.count("A") + 
          word.count("e") + word.count("E") + 
          word.count("i") + word.count("I") + 
          word.count("o") + word.count("O") + 
          word.count("u") + word.count("U"))
