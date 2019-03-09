file_read = open("invocations.txt", "r")

file_write = open("invocation_comma.txt", "a")

lines = file_read.readlines()

for string in range(0, len(lines)):
	inp = lines[string]
	write1 = inp[:inp.find(";")]
	write2 = inp[inp.find(";") + 1:]

	file_write.write(write1 + "," + write2)

file_read.close()
file_write.close()

