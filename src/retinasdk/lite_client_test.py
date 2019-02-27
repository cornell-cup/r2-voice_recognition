import retinasdk

apiKey = "ac486a40-3220-11e9-bb65-69ed2d3c7927"

liteClient = retinasdk.LiteClient(apiKey)

keyPhrase = "R2, give me a coke from the fridge"

keywords = liteClient.getKeywords(keyPhrase)

for x in range (0, len(keywords)):
	print (keywords[x])



	
