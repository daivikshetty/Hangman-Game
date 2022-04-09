import randomword

count=7
arr=[]

word=randomword.return_word()

for i in range(0,len(word)):
      if word[i]==" ":
            arr.insert(i," ")
            continue
      arr.insert(i,"_")

def printArr():
      print()
      for i in arr:
            print(i,end="\t")
      print()

def remGuess():
      remaining=0
      for i in arr:
            if i=="_":
                  remaining+=1

      return remaining


printArr()

while count!=0:
      print()
      print()
      print(f"Remaining Lives : {count}")
      guessLetter=input("Guess a letter : ")
      guessLetter=guessLetter.upper()

      if guessLetter in word:
            for i in range(0,len(word)):
                  if word[i]==guessLetter:
                        arr[i]=guessLetter

            printArr()
      else:
            count-=1
            printArr()

      if count==0:
            print("You Lose.Game Over.")
            break

      if remGuess()==0:
            print("You Win")
            break

