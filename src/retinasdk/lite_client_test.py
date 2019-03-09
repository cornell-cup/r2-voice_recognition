import retinasdk

apiKey = "ac486a40-3220-11e9-bb65-69ed2d3c7927"

liteClient = retinasdk.LiteClient(apiKey)

file_object = open("invocations.txt", "a")

while (True):
	keyPhrase = raw_input("enter a command: ")

	keywords = liteClient.getKeywords(keyPhrase)
	
	file_object.write(keyPhrase + ", ")

	if "high five" in keyPhrase:
		print ("high five")
		file_object.write("high five, ")

	else:
		for x in range (0, len(keywords)):
			print (keywords[x])
			file_object.write(keywords[x] + ", ")
	
	file_object.write("\n")
		
file_object.close()
		
		



	
