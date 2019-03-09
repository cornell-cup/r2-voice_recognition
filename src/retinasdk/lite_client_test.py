import retinasdk

apiKey = "ac486a40-3220-11e9-bb65-69ed2d3c7927"

liteClient = retinasdk.LiteClient(apiKey)

#file_read_object = open("SayingList.csv", "r")
file_object = open("invocations.txt", "a")

#keyPhrase = file_read_object.read()

count = 0

#while ((keyPhrase != None) or (keyPhrase != "")):
while (True):
    
#	print (count)
#	count = count + 1
#	keyPhrase = keyPhrase[keyPhrase.find(",", keyPhrase.find(",") + 1):]
    
#	print (keyPhrase)
	keyPhrase = input("enter a command: ")

	keywords = liteClient.getKeywords(keyPhrase)
	file_object.write(keyPhrase + ";")

	if "high five" in keyPhrase:
		print ("high five")
		file_object.write("high five;")

	else:
		for x in range (0, len(keywords)):
			print (keywords[x])
			file_object.write(keywords[x] + ";")
	
	file_object.write("\n")

	if (keyPhrase == "stop"):
		break;

#	keyPhrase = file_read_object.read()

#file_read_object.close()
		
file_object.close()
		
		



	
