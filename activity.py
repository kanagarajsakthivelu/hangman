from random import choice

def word_generator():
    with open("wordlist.py","r") as f:
        lines=f.readlines()
    f.close()
    lines= [i.strip("\n") for i in lines]
    return choice(lines)

word_generator()

word= word_generator()
guessed=""
turns=int(len(word)*1.5)

while(True):    
    print("you're left with {} turns".format(turns))
    inp=input("\nMake a guess: ")
    turns=turns-1
    if inp in word:
        guessed=guessed+inp
    unguessed_char=0
    for i in word:
        if i in guessed:
            print(i,end="")
        else:
            unguessed_char+=1
            print("*",end="")
    if unguessed_char==0:
        print("\n Hurray!! you won...")
        break
    if turns==0:
        print("\ntoin toin toin.... you ran out of attempt")
        break
