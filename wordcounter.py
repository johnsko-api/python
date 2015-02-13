message = "hello hello hello my name is"
wordcount={}
for word in message.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print k, v

print wordcount
