sentence=input("write sentence ")
# words=sentence.split()
# length_sentence=[len(word)  for word in words]
# print(length_sentence)




words=[]
i=0
count=0
while i <len(sentence):
    if sentence[i] !=" ":
        count+=1
    else:
        words.append(count)
        count=0
    i+=1
print(words)
    

