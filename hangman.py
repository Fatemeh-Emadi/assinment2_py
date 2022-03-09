import random

words_bank=["book","tree","apple","sadjad","linux","iran","mashhad","blue","python","computer"];

#index=random.randint(0,9)

#word=words_bank[index]
word=random.choice(words_bank)
user_true_chars=[]
joon=5
while(True):
    for i in range(len(word)):
        if word[i] in user_true_chars:
            print(word[i],end="")
        else:
            print("_",end="")

    print("\n please enter character:")
    user_char=input()


    if user_char in word:
        user_true_chars.append(user_char)
        print("y")
    else:
        joon-=1
        print("n")
    
    if joon==0:
        print("game over")
        break
    
    if (len(user_true_chars) ==len( word)):
        print("The word is",word,end="")
        print("\n win")
        break
