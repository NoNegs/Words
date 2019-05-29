def Wordcount(Message):
	word=1
	i=0
	while i<len(Message):
		if Message[i]==" ":
			word+=1
		i+=1
	return word
print("Words: ",Wordcount("Hello My Friends"))
print("Words: ",Wordcount("I am Back Forever"))
	
	