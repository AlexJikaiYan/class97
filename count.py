sentence = input("enter a sentence :") 
print(sentence) 
charactercount = 0
wordcount=1
for i in sentence:
    charactercount = charactercount+1
    if(i==" "):
        wordcount=wordcount+1
print("characters:",charactercount)
print("words:",wordcount)