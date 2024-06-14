text_file=open('sometext-1.txt','r')

word_count={}

read_text=text_file.read()
words=read_text.split()

for word in words:
    if word not in word_count:
        word_count[word]=1
    else:
        word_count[word]+=1

print(word_count)




#word_count=0
#for word in text_file:
   # print(word)
#words={}

#count=word_count[]+1


#read file
#create dictionary
#iterate through each word of file
#if word is not in dictionary, add it as a key, and add 1 to its value
#