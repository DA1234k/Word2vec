import numpy as np
import matplotlib.pyplot as plt


X=[]
f = open("64830.txt","r")
for i in f:
	if i=='\n\n':
		continue
	X.append(i.strip().split())


all_words = set(w for words in X for w in words)
glove={}
total_words=[]
with open("glove.840B.300d.txt","rb") as f1:
	for f2 in f1:
		parts = f2.split()
		word = parts[0].decode("utf8")
		if (word in all_words):
			nums=np.array(parts[1:], dtype=np.float64)
			total_words.append(word)
			glove[word] = nums
	#words_np=list(all_words-set(total_words))


#print(total_words)
print(len(total_words))
#print(glove)
#plt.plot(total_words,"ro")
#plt.show()