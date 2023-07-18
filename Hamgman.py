import time
import random
var6 = 0
var7 = 0
var8 = 0
wrong_answers = 0

def hangman():
  if wrong_answers==0:
    print("\n"*40)
    print("   _________ ")
    print("   |       | ")
    print("           | ")
    print("           | ")
    print("           | ")
    print("           | ")
    print("           | ")
    print("  |||||||||||")
    print(" ||||||||||||") 
  if wrong_answers==1:
    print("\n"*40)
    print("   _________ ")
    print("   |       | ")
    print("   0       | ")
    print("           | ")
    print("           | ")
    print("           | ")
    print("           | ")
    print("  |||||||||||")
    print(" ||||||||||||")
  if wrong_answers==2:
    print("\n"*40)
    print("   _________ ")
    print("   |       | ")
    print("   0       | ")
    print("   |       | ")
    print("           | ")
    print("           | ")
    print("           | ")
    print("  |||||||||||")
    print(" ||||||||||||")
  if wrong_answers==3:
    print("\n"*40)
    print("   _________ ")
    print("   |       | ")
    print("   0       | ")
    print("   |       | ")
    print("   |       | ")
    print("           | ")
    print("           | ")
    print("  |||||||||||")
    print(" ||||||||||||")
  if wrong_answers==4:
    print("\n"*40)
    print("   _________ ")
    print("   |       | ")
    print("   0       | ")
    print("   |       | ")
    print("   |       | ")
    print("  /        | ")
    print("           | ")
    print("  |||||||||||")
    print(" ||||||||||||")
  if wrong_answers==5:
    print("\n"*40)
    print("   _________ ")
    print("   |       | ")
    print("   0       | ")
    print("   |       | ")
    print("   |       | ")
    print("  / \      | ")
    print("           | ")
    print("  |||||||||||")
    print(" ||||||||||||")
  if wrong_answers==6:
    print("\n"*40)
    print("   _________ ")
    print("   |       | ")
    print("   0       | ")
    print("  /|       | ")
    print("   |       | ")
    print("  / \      | ")
    print("           | ")
    print("  |||||||||||")
    print(" ||||||||||||")
  if wrong_answers==7:
    print("\n"*40)
    print("   _________ ")
    print("   |       | ")
    print("   0       | ")
    print("  /|\      | ")
    print("   |       | ")
    print("  / \      | ")
    print("           | ")
    print("  |||||||||||")
    print(" ||||||||||||")
  if wrong_answers==8:
    print("\n"*40)
    print("   _________ ")
    print("   |       | ")
    print("   0       | ")
    print("  /|\      | ")
    print(" * |       | ")
    print("  / \      | ")
    print("           | ")
    print("  |||||||||||")
    print(" ||||||||||||")
  if wrong_answers==9:
    print("\n"*40)
    print("  You died   ")
    print("   _________ ")
    print("   |       | ")
    print("   0       | ")
    print("  /|\      | ")
    print(" * | *     | ")
    print("  / \      | ")
    print("           | ")
    print("  |||||||||||")
    print(" ||||||||||||")



word_list = ["abroad", "become", "entity", "doctor", "year", "fluid", "level", "metal"]
#More words can be added here
var2 = random.randint(0,len(word_list)-1) 
word = word_list[var2] 
answer = ""
for let in word:
  answer = answer + let + " " #This just puts spaces in the word

if len(word) == 6:
  shown = "_ _ _ _ _ _"
elif len(word) == 5:
  shown = "_ _ _ _ _"
else:
  shown = "_ _ _ _"
hangman()
print("You have 9 guesses before you run out!")
print(shown)
letter = input("(guess a letter) ?: ").lower()
while True:
  var6 += 1
  if var6 >= 2:
    letter = input("?: ").lower()
  var3 = int(0)
  var4 = int(0)
  var5 = int(0)
  var7 = int(0)
  for let in word:
    if let == letter:
      var3 += 1
    elif var3 == 0:
      var4 += 1
      var5 = var4
    elif var3 == 1:
     var5 += 1
  if var3 == 0:
   wrong_answers += 1
   hangman()
   print ("Sorry, no match")
   print (shown)
  elif var3 == 1:
    hangman()
    print ("There is one of that letter")
    shown = shown[:var4*2] +  letter + shown[var4*2+1:]
    print (shown)
  elif var3 == 2:
    hangman()
    print ("There are two of that letter")
    shown = shown[:var4*2] +  letter + shown[var4*2+1:]
    shown = shown[:var5*2+2] +  letter + shown[var5*2+3:] 
    print (shown)

  if shown + " " == answer: 
    print("\n"*40)
    print("   _________ ")
    print("   |       | ")
    print("           | ")
    print("           | ")
    print("           | ")
    print("           |  . 0 .")
    print("           |   \|/")
    print("  |||||||||||   |")
    print(" ||||||||||||  / \ ")
    print ("Congratulations!")
    var8 = 1
    break
  if wrong_answers >= 9 and var8 == 0:
    print ("Too bad, the word was '" + word + "'!")
    break
